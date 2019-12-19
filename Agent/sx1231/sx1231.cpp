#include <wiringPi.h>
#include <wiringPiSPI.h>

template< int N, int S =0 >
class SpiDev {
  public:
    static void master (int div) {
      wiringPiSetup();
      wiringPiSPISetup (N, 4000000);
    }

    static uint8_t rwReg (uint8_t cmd, uint8_t val) {
      uint8_t data[2] = { cmd, val };
      if (wiringPiSPIDataRW (N, data, 2) == -1) {
        printf("SPI error\n");
        return 0;
      }
      return data[1];
    }
};

typedef SpiDev<0> SpiDev0;
typedef SpiDev<1> SpiDev1;


RF69<SpiDev0> rf;
