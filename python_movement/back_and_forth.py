import sys, traceback
import serial
import time
def main(serCom):
	try:
		UserCmd = "<01>\r"
		serCom.write(UserCmd.encode())
		CtrlReply = serCom.read(128)
		if len(CtrlReply) > 0:
			print("   " + CtrlReply.decode('utf-8'))
			print("    Successful connect")
		else:
			print("no reply")
		print("preparing to loop, setting back to 0 position...")
		UserCmd = "<08 00000000>\r"
		serCom.write(UserCmd.encode())
		CtrlReply = serCom.read(128)
		if len(CtrlReply) > 0:
			print("   " + CtrlReply.decode('utf-8'))
		else:
			print("   no reply")
		#forward movement loop
		UserCmd = '<06 1 00000064>\r'
		for i in range(30):
			serCom.write(UserCmd.encode())
			CtrlReply = serCom.read(128)
			time.sleep(0.25)
		#backward movement
		UserCmd = '<06 0 00000064>\r'
		for i in range(30):
			serCom.write(UserCmd.encode())
			CtrlReply = serCom.read(128)
			time.sleep(0.25)
	except KeyboardInterrupt:
		print('deuce')
		serCom.close()
		sys.exit(0)
	except Exception:
		traceback.print_exc(file=sys.stdout)
		serCom.close()
		sys.exit(0)
