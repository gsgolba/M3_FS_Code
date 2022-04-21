CXX = g++
INCLUDES = -I ../include
OBJECTS = whale.o keyboard_movement.o serial.o unix.o
%.o: %.cpp
	$(CXX) -c -o $@ $< $(INCLUDES)
%.o: %.cc
	$(CXX) -c -o $@ $< $(INCLUDES)
whale: $(OBJECTS)
	$(CXX) -o whale $(OBJECTS)

.PHONY: clean

clean:
	-rm -f $(OBJECTS)
