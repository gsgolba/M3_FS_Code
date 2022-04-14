import time
import sys
import serial
import numpy as np
from pymavlink import mavutil
def main():
	print('start')
	master = mavutil.mavlink_connection('/dev/serial0', baud=921600)
	master.wait_heartbeat()
	master.mav.param_request_list_send(master.target_system, master.target_component)
	#begin_time = time.time()
	try:
		message = master.recv_match(type='GPS_RAW_INT', blocking=True).to_dict()
	except Exception as error:
		print(error)
		#serCom.close()
		sys.exit(0)
	print(message)
	base_alt = message['alt']
	base_lon = message['lon']
	base_lat = message['lat']
	print('Base altitude, longitude and latitude \r\n Altitude: ', base_alt, '\r\n Longitude: ', base_lon, '\r\n Latitude: ', base_lat)
	print("before loop")
	while True:
		try:
			message = master.recv_match(type='GPS_RAW_INT', blocking=True).to_dict()
			#print(time.time())
			print("Altitude: ", message['alt'])
			print('Longitude: ', message['lon'])
			print('Latitude: ', message['lat'])
			alt_diff = float(base_alt - message['alt']) #altitude is m^3 E3
			lon_diff = float(base_lon - message['lon']) #lon and lat are degrees E7
			lat_diff = float(base_lat - message['lat'])
			print('The altitude difference is: ', alt_diff)
			print('In meters this would be: ', alt_diff / 1000, 'meters')
			print('The longitude difference is: ', lon_diff) #Estimate one second(degrees) to be around 30.87 meters
			print('In meters this would be: ', lon_diff * 3600 * 30.87 / 10000000, 'meters')
			print('The latitude difference is: ', lat_diff)
			print('In meters this would be: ', lat_diff * 3600 * 30.87 / 10000000, 'meters \r\n')
			time.sleep(0.5)
		except KeyboardInterrupt:
			print("keyboard interrupt")
			#serCom.close()
			sys.exit(0)
		except Exception as error:
			print(error)
			print('bruh')
			#serCom.close()
			sys.exit(0)
if __name__ == '__main__':
	print("don't run on its own, we have no serCom connection. Fix that first")
	main()
	#graph_testing()
