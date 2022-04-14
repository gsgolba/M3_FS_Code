import sys, traceback
import serial
import time
def main(serCom):
    try:
        UserCmd = "<01>\r"
        serCom.write(UserCmd.encode())
        CtrlReply = serCom.read(128)
        if len(CtrlReply) > 0:
            print ("    " + CtrlReply.decode('utf-8'))
            print("      Successfully connected!")
        else:
            print("    no reply from controller")
        print( 'Enter your commands below at the >> prompt.\r\n Commands: \r\n      exit: stops the program \r\n      status: tells you the current position of the lens \r\n      d: move lens forward (about 85 micrometers) \r\n      dd: move lens slighty forward (about 4 micrometers) \r\n      a: move lens backward (about 85 micrometers) \r\n      aa: move lens slightly backward (about 4 micrometers) \r\n      spot: [integer between 0 and 3000]: move lens to a desired position (goes in half micrometer steps)')
        while(True):
            UserCmd = raw_input('enter command: ')
            UserCmd = unicode(UserCmd,"utf-8")
            for i in range(1): #get rid of this for loop, it is useless
                words = UserCmd.split(" ")
                for word in words:
                    print(word)
                    if word == 'd':
                        #move forward
                        print("forward movement")
                        UserCmd = '<06 1 000000A9>\r'
                        serCom.write(UserCmd.encode())
                        CtrlReply = serCom.read(128)
                        if len(CtrlReply) > 0:
                            print('     ' + CtrlReply.decode('utf-8'))
                        else:
                            print('     No reply from controller')
                        time.sleep(0.25)
                    elif word == 'dd':
                        #move slightly forward
                        print("slight forward movement")
                        UserCmd = '<06 1 00000009>\r'
                        serCom.write(UserCmd.encode())
                        CtrlReply = serCom.read(128)
                        if len(CtrlReply) > 0:
                            print('     ' + CtrlReply.decode('utf-8'))
                        else:
                            print('     No reply from controller')
                        time.sleep(0.25)
                    elif word == 'a':
                        #move backward
                        print("backward movement")
                        UserCmd = '<06 0 000000A9>\r'
                        serCom.write(UserCmd.encode())
                        CtrlReply = serCom.read(128)
                        if len(CtrlReply) > 0:
                            print('     ' + CtrlReply.decode('utf-8'))
                        else:
                            print('     No reply from controller')
                        time.sleep(0.25)
                    elif word == 'aa':
                        #move slightly backward
                        print("slight backward movement")
                        UserCmd = '<06 0 00000009>\r'
                        serCom.write(UserCmd.encode())
                        CtrlReply = serCom.read(128)
                        if len(CtrlReply) > 0:
                            print('     ' + CtrlReply.decode('utf-8'))
                        else:
                            print('     No reply from controller')
                        time.sleep(0.25)
                    elif word == 'spot':
                        index = words.index('spot')
                        if 0 <= index + 1 < len(words):
                            if words[index + 1].isnumeric() == False:
                                print("spot must be accompanied by some number (0 - 3000)")
                            elif int(words[index + 1]) < 0 or int(words[index + 1]) > 3000:
                                print("please choose a number between 0 and 3000 (initial encoder count goes by 0.5 micrometer steps)")
                            else:
                                UserCmd = '<08 ' + format(int(words[index + 1]), '08x') + '>\r'
                                serCom.write(UserCmd.encode())
                                CtrlReply = serCom.read(128)
                                if len(CtrlReply) > 0:
                                    print("     " + CtrlReply.decode('utf-8'))
                                else:
                                    print("      no reply from controller")
                        else:
                            print("accompany spot with an integer (0 - 3000)")
                        time.sleep(0.5)
                    elif word == 'status':
                        UserCmd = "<10>\r"
                        serCom.write(UserCmd.encode())
                        CtrlReply = serCom.read(128)
                        if len(CtrlReply) > 0:
                            print ("you are in position " + str(int(CtrlReply.decode("utf-8")[11:19], 16) / 2) + " in micrometers (can go to 1500)")
                        else:
                            print("   No reply from controller")
                    elif word == "exit":
                        #exit the program 
                        print("peace")
                        serCom.close()
                        sys.exit(0)
                    else:
                        if word.isnumeric() == False:
                            print("not a valid command")
    except KeyboardInterrupt:
        print("leave")
        serCom.close()
        sys.exit(0)
    except Exception:
        traceback.print_exc(file=sys.stdout)
        serCom.close()
        sys.exit(0)


if __name__ == "__main__":
    #we don't wanna run main solely from this
    print("this module should be imported and used in the other file")
