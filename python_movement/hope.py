import sys
import time
import serial
import keyboard_input
#import pymavlink_testing
import back_and_forth
# Default COM port
ComPort = '/dev/ttyUSB0'
# PX4 port connection
px4_port = '/dev/serial0'
# If an extra argument was specified (besides the name of the script), assume its a port name
if len(sys.argv) > 1:
    ComPort = sys.argv[1]
# configure the serial connection
#print(ComPort)
try:
    ser = serial.Serial(port=ComPort,
                        baudrate=115200,
                        parity=serial.PARITY_NONE,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.EIGHTBITS)
except Exception as e:
    print(e)
    print ("Failed to open COM port " + ComPort)
    exit()

# Should get a reply within 100 msec!
ser.timeout = 0.1

# Just a prompt
print( 'Enter your commands below at the >> prompt.\r\nTo stop, type exit.')
print('you can do regular <> command, keyboard, or loop.')
# Accept commands until the user enters 'exit'
while 1 :

    # get keyboard input (using "raw_input" so that quotes are not required)
    UserCmd = raw_input('>> ')
    print(UserCmd)
    # Request to exit?
    if UserCmd == 'exit':
        ser.close()
        exit()
#Probably delete this below, I doubt we'll need to message the transciever
    # Message to transceiver?
    elif UserCmd[:2] == 'TR':
        UserCmd = UserCmd[2:] + '\r'
        b = bytearray(UserCmd)
        l = len(b)
        i = 0

		# OR in bit 7 so that the transceiver processes the command
        while i < l:
            b[i] = b[i] | 0x80
            i = i + 1
        ser.write(b)		
        # fetch the reply
        CtrlReply = ser.read(128)

        #show the reply but must decode to make it a string
        print ("   " + CtrlReply.decode("utf-8"))

    #Start of a normal command?
    elif UserCmd[:1] == '<':
        # send the character to the device (but first append a CR)
        UserCmd = UserCmd + '\r' 
        #print(UserCmd)
        #print(ser.write(UserCmd.encode()))
        ser.write(UserCmd.encode())  #convert string to byte array

        # fetch the reply
        CtrlReply = ser.read(128)
        if len(CtrlReply) > 0:
            print ("   " + CtrlReply.decode("utf-8"))
        else:
            print ("   No reply from controller")


    elif UserCmd == 'keyboard':
        print("buckle up")
        keyboard_input.main(ser)

    elif UserCmd == 'loop':
        #back and forth loop
        back_and_forth.main(ser)

