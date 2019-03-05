RADIOHEAD=/home/ulf/repository/RadioHead

rf_69_test:cat_agent.o rf69_test.o
	gcc -o rf69_test cat_agent.o rf69_test.o

cat_agent.o:cat_agent.cpp
	gcc -c -I ${RADIOHEAD} cat_agent.cpp

rf69_test.o:rf69_test.cpp
	gcc -c -I ${RADIOHEAD} rf69_test.cpp

