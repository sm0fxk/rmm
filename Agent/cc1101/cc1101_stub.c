#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "main.h"
#include "radio.h"
#include "cc1101.h"

uint8_t cc1101_register[64];

void init()
{
	
}

void get_radio_model(char* reply)
{
    sprintf(reply, "CC110x\n");

}

void get_modem_config(char* reply)
{
    sprintf(reply, "['OOK','2-FSK','4-FSK','MSK','GFSK']\n");
    
}

void get_transmit_power(char* reply)
{
    sprintf(reply, "['-30', '-20', '-15', '-10', '0', '5', '7','10']\n");

}

void get_trcv_register_range(char* reply)
{

    sprintf(reply, "(00,62)\n");

}

int get_trcv_register(int reg, char* reply)
{
     return(cc1101_register[reg]);

}

int set_trcv_register(unsigned int reg, unsigned int value)
{
    cc1101_register[reg] =value;
    return(value);

}

uint32_t get_frequency()
{
	uint8_t freq0 = 0;
	uint8_t freq1 = 0;
	uint8_t freq2 = 0;
	
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

