OBJS = ../lib/cat_agent_net.o  cc1101_glue.o pi_cc_spi.o radio.o util.o 
OBJS_STUB = ../lib/cat_agent_net.o cc1101_stub.o

cat_agent: $(OBJS)
	gcc $(LDFLAGS) -s -lm -lwiringPi -o cat_agent $(OBJS) 

stub: cat_agent_stub

cat_agent_stub: $(OBJS_STUB)
	gcc -o cat_agent_stub $(OBJS_STUB)

cat_agent.o:cat_agent.c
	gcc -c  cat_agent.c

cc1101_glue.o: cc1101_glue.c
	gcc -c cc1101_glue.c

cc1101_stub.o: cc1101_stub.c
	gcc -c cc1101_stub.c


pi_cc_spi.o:pi_cc_spi.h pi_cc_spi.c
	$(CCPREFIX)gcc $(CFLAGS)  -c -o pi_cc_spi.o pi_cc_spi.c

radio.o: radio.h radio.c
	$(CCPREFIX)gcc $(CFLAGS)  -c -o radio.o radio.c

util.o: util.h util.c
	$(CCPREFIX)gcc $(CFLAGS) -c -o util.o util.c


clean:
	rm -f cat_agent $(OBJS)
	
