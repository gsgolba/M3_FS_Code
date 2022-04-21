#include "keyboard_movement.h"
//check is string is purely numbers
bool is_number(const std::string& s){
	std::string::const_iterator it = s.begin();
	while (it != s.end() && std::isdigit(*it))
		++it;
	return !s.empty() && it == s.end();
}
//make number hexadecimal
std::string int_to_hex(const int & i){
	std::stringstream ss;
	ss << std::uppercase << std::setfill('0') << std::setw(8) << std::hex << i;
	return ss.str();
}
//make number decimal
int hex_to_int(const std::string & s){
	int n = 0;
	std::stringstream ss;
	ss << s;
	ss >> std::hex >> n;
	return n;
}
void keyboard(serial::Serial & serial_){
	std::string input;
	std::cout << "Mystical Keyboard Inputting: Commands \n \n";
        std::cout << "The lens can move in a range of positions between 0 to 3000 micrometers \n";
        std::cout << "d: Move the lens approixmately 100 micrometers forward \n";
        std::cout << "dd: Move the lens approixmately 10 micrometers forward \n";
        std::cout << "a: Move the lens approixmately 100 micrometers backward \n";
        std::cout << "aa: Move the lens approixmately 10 micrometers backward \n";
        std::cout << "[some number between and including 0 to 3000]: moves the lens to that micrometer position \n";
        std::cout << "status: tells you the current position of the lens \n";
	std::cout << "exit: leaves keyboard usage" << std::endl;
	while (getline(std::cin, input) && input != "exit"){
		if (input == "d"){
			serial_.write("<06 1 00000064>\r");
		}
	        else if (input == "dd"){
	                serial_.write("<06 1 0000000A>\r");
		}
	        else if (input == "a"){
	                serial_.write("<06 0 00000064>\r");
		}
	        else if (input == "aa"){
	                serial_.write("<06 0 0000000A>\r");
		}
                else if (is_number(input)){
                        int value_ = std::stoi(input);
			if ((value_ >= 0) && (value_ <= 3000)){
				input = int_to_hex(value_);
				serial_.write("<08 " + input + ">\r");
			}
			else
				std::cout << "make sure the number is between 0 and 3000" << std::endl;
                }
		else if (input == "status"){
			//clear out the buffer of things we haven't read
			serial_.readline(50);
			serial_.write("<10>\r");
			std::string return_ = serial_.readline(20).substr(11,8);
			int n = hex_to_int(return_);
			std::cout << "position " << std::to_string(n) << " in 0.5 micrometers (from 0 to 3000)" << std::endl;
		}
		else {
			std::cout << "Not a valid command";
		}
	}
	return;
}
