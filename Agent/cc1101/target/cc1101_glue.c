#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "main.h"

char *modulation_names[] = {
    "OOK",
    "2-FSK",
    "4-FSK",
    "MSK",
    "GFSK",
};

uint32_t rate_values[] = {
    50,
    110,
    300,
    600,
    1200,
    2400,
    4800,
    9600,
    14400,
    19200,
    28800,
    38400,
    57600,
    76800,
    115200,
    250000,
    500000
};

uint8_t nb_preamble_bytes[] = {
    2,
    3,
    4,
    6,
    8,
    12,
    16,
    24
};

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

