
#include <inttypes.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*
void init();
void get_radio_model(char*);
*/

void init_spi();
uint8_t readReg(uint8_t);
void writeReg(uint8_t, uint8_t);


void init()
{
    init_spi();
}

void get_radio_model(char* reply)
{
    sprintf(reply, "sx1231/sx1231h\n");

}


void get_trcv_register_range(char* reply)
{

    sprintf(reply, "(00,62)\n");

}

uint8_t get_trcv_register(uint8_t reg, char* reply)
{
    uint8_t value;

     value = readReg(reg);
     printf("Register value = %02x\n", value);
     return(value);
}

int set_trcv_register(uint8_t reg, uint8_t value)
{
    writeReg(reg, value);
    return(value);

}

int set_frequency(uint32_t freq_hz)
{

    return(0);
}

int get_trcv_status()
{
	return(1);        
}

void get_modem_config(char* reply)
{
    sprintf(reply, "['OOK']\n");
    printf("'2-FSK',");
    printf("'4-FSK',");
    printf("'MSK',");
    printf("'GFSK']\n");
	}


void get_transmit_power(char* reply)
{
    sprintf(reply, "['-30', '-20', '-15', '-10', '0', '5', '7','10']\n");

}


void	set_trcv_status(char *args)
{
}



