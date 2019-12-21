#include <iostream>
#include <wiringPiSPI.h>

#define SPI_CHANNEL 0
#define SPI_CLOCK_SPEED 1000000


static uint8_t rwReg (uint8_t cmd, uint8_t val) {
        uint8_t data[2] = { cmd, val };
#if 1
        if (wiringPiSPIDataRW (SPI_CHANNEL, data, 2) == -1) {
            printf("SPI error\n");
            return 0;
        }
#else
        Chunk xfer = { 2, data, data };
        pseudoDma(&xfer, 1);
#endif
        printf("spi data: %x\n", data[1]);
        return data[1];
    }





uint8_t readReg (uint8_t addr) {
      return rwReg(addr, 0);
    }

void writeReg (uint8_t addr, uint8_t val) {
      rwReg(addr | 0x80, val);
    }


int init_spi()
{
    int fd = wiringPiSPISetupMode(SPI_CHANNEL, SPI_CLOCK_SPEED, 0);
    if (fd == -1) {
        printf("Failed to init SPI communication.\n");
        return -1;
    }
    printf("SPI communication successfully setup.\n");
   
    return 0;
}