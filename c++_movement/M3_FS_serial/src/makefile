CXX = g++
INCLUDES = -I ../include
OBJECTS = manual_control.o keyboard_movement.o serial.o unix.o
%.o: %.cpp
	$(CXX) -c -o $@ $< $(INCLUDES)
%.o: %.cc
	$(CXX) -c -o $@ $< $(INCLUDES)
manual_control: $(OBJECTS)
	$(CXX) -o manual_control $(OBJECTS)

.PHONY: clean

clean:
	-rm -f $(OBJECTS)
