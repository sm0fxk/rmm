#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "main.h"
#include "radio.h"

arguments_t   arguments;
//serial_t      serial_parameters;
spi_parms_t   spi_parameters;
radio_parms_t radio_parameters;


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

// ------------------------------------------------------------------------------------------------
// Init arguments
static void init_args(arguments_t *arguments)
// ------------------------------------------------------------------------------------------------
{
    arguments->verbose_level = 0;
    arguments->print_long_help = 0;
    arguments->serial_device = 0;
    arguments->serial_speed = B38400;
    arguments->serial_speed_n = 38400;
    arguments->spi_device = 0;
    arguments->print_radio_status = 0;
    arguments->modulation = MOD_FSK2;
    arguments->rate = RATE_9600;
    arguments->rate_skew = 1.0;
    arguments->packet_delay = 30;
    arguments->modulation_index = 0.5;
    arguments->freq_hz = 433600000;
    arguments->packet_length = 250;
    arguments->variable_length = 0;
    arguments->test_mode = TEST_NONE;
    arguments->test_phrase = strdup("Hello, World!");
    arguments->repetition = 1;
    arguments->fec = 0;
    arguments->whitening = 0;
    arguments->preamble = PREAMBLE_4;
    arguments->tnc_serial_window = 40000;
    arguments->tnc_radio_window = 0;
    arguments->tnc_keyup_delay = 4000;
    arguments->tnc_keydown_delay = 0;
    arguments->tnc_switchover_delay = 0;
    arguments->real_time = 0;
}

// ------------------------------------------------------------------------------------------------
// Delete arguments
void delete_args(arguments_t *arguments)
// ------------------------------------------------------------------------------------------------
{
    if (arguments->serial_device)
    {
        free(arguments->serial_device);
    }
    if (arguments->spi_device)
    {
        free(arguments->spi_device);
    }
    if (arguments->test_phrase)
    {
        free(arguments->test_phrase);
    }
}



void init()
{
    int ret;

    init_args(&arguments); 
    arguments.spi_device = strdup("/dev/spidev0.0");
    init_radio_parms(&radio_parameters, &arguments);
    ret = init_radio(&radio_parameters, &spi_parameters, &arguments);
    if (ret != 0)
    {
        fprintf(stderr, "PICC: Cannot initialize radio link, RC=%d\n", ret);
        delete_args(&arguments);

    }
}



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

uint8_t get_trcv_register(uint8_t reg)
{
    uint8_t reg_value;
    PI_CC_SPIReadReg(&spi_parameters, reg, &reg_value); 
    return(reg_value);

}

int set_trcv_register(int reg, int value)
{

	     return(0);

}

