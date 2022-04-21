#include <string>
#include <iostream>
#include <cstdio>
#include <unistd.h>
#include "serial.h"
#include "keyboard_movement.h"

int main(){
	std::string port_ = "/dev/ttyUSB0";
	unsigned long baud_rate = 115200;
	//assume parity(none), byte size(8), and stopbits(1) are standard
	std::cout << "Testing opening..." << std::endl;
	serial::Serial m3_fs(port_, baud_rate, serial::Timeout::simpleTimeout(1000));
	if (m3_fs.isOpen())
		std::cout << "Port is open" << std::endl;
	else{
		std::cout << "Port did not open, we will close" << std::endl;
		m3_fs.close();
		return 1;
	}
	std::cout << "Sending motor inquiry" << std::endl;
	std::string message_ = "<01>\r";
	m3_fs.write(message_);
	std::string output_ = m3_fs.readline(); //not sure how large to make it read
	std::cout << "Output is: " << output_ << std::endl;
	std::cout << "Trying keyboard function" << std::endl;
	keyboard(m3_fs);
	m3_fs.close();
	return 0;
}
