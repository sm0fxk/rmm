#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "main.h"
#include "radio.h"
#include "cc1101.h"


void init()
{
	
}

void get_radio_model()
{
    fputs("CC110x\n", stdout);

}

void get_modem_config()
{
	printf("['OOK',");
    printf("'2-FSK',");
    printf("'4-FSK',");
    printf("'MSK',");
    printf("'GFSK']\n");
	}

void get_transmit_power()
{
    printf("['-30', '-20', '-15', '-10', '0', '5', '7','10']\n");

}

int get_trcv_register_range()
{
}

int get_trcv_register(int reg)
{
         return(0x2b);

}

int set_trcv_register(int reg, int value)
{

	     return(0);

}

int set_frequency(uint32_t freq_hz)
{

    return(0);
}

int get_trcv_status()
{
	        
	}
	
void	set_trcv_status(char *args)
{
}

