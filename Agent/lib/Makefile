all: cat_agent_net.o spilib.o

cat_agent_net.o: cat_agent_net.c
	g++ -c cat_agent_net.c

spilib.o: spilib.cpp
	g++ -c spilib.cpp
clean:
	rm *.o
