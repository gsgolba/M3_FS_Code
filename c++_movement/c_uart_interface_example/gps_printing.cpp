#include <iostream>
#include <common/mavlink.h>
#include "autopilot_interface.h"
#include "serial_port.h"
#include "udp_port.h"
#include <sys/time.h>
#include <time.h>
int main(){
	char * uart_name = (char*)"/dev/serial0";
	int baudrate = 921600;
	Generic_Port *port;
	port = new Serial_Port(uart_name, baudrate);
	Autopilot_Interface ai(port);
	port->start();
	printf("port open\n");
	ai.start();
	printf("sus\n");
	for (int i = 0; i < 10; ++i){
		printf("in for loop\n");
		while (not (ai.current_messages.time_stamps.global_position_int)){
		//while (not (ai.current_messages.time_stamps.local_position_ned)){
			printf("in loop\n");
			usleep(500000);
		}
		printf("lat, lon, alt: %zu , %zu, %zu \n", ai.current_messages.global_position_int.lat, ai.current_messages.global_position_int.lon, ai.current_messages.global_position_int.alt);
	}
	ai.stop();
	port->stop();
	delete port;

	std::cout << "nice" << std::endl;
	return 0;
}
