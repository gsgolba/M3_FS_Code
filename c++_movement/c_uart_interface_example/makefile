all: git_submodule mavlink_control man

mavlink_control: mavlink_control.cpp serial_port.cpp udp_port.cpp autopilot_interface.cpp
	g++ -g -Wall -I mavlink/include/mavlink/v2.0 mavlink_control.cpp serial_port.cpp udp_port.cpp autopilot_interface.cpp -o mavlink_control -lpthread

git_submodule:
	git submodule update --init --recursive
man: gps_printing.cpp serial_port.cpp udp_port.cpp autopilot_interface.cpp
	g++ -g -Wall -I mavlink/include/mavlink/v2.0 gps_printing.cpp serial_port.cpp udp_port.cpp autopilot_interface.cpp -o man -lpthread
clean:
	 rm -rf *o mavlink_control
