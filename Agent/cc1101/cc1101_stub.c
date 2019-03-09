#include <stdio.h>
#include <stdlib.h>
#include <string.h>



void get_radio_model()
{
    fputs("CC110x\n", stdout);

}

void get_modem_config()
{
	printf("['GFSK, Data Rate: 1.2kBaud, Dev: 5.2kHz, RX BW 58kHz',");
	printf("'GFSK, Data Rate: 2.4kBaud, Dev: 5.2kHz, RX BW 58kHz']\n");
	}

void get_transmit_power()
{
    printf("['-30', '-20', '-15', '-10', '0', '5', '7','10']\n");

}

int get_trcv_register(int reg)
{
         return(0x2b);

}

int set_trcv_register(int reg, int value)
{

	     return(0);

}

