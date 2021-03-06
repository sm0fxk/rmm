{"model": "CC110x",
 "description": {"modulation":"GFSK", "speed": "100kb/s","rx_bw":"00", "deviation":"5kHz"},
"registers" : [ 
    0x07,  # IOCFG2        GDO2 Output Pin Configuration
    0x2E,  # IOCFG1        GDO1 Output Pin Configuration
    0x80,  # IOCFG0        GDO0 Output Pin Configuration
    0x07,  # FIFOTHR       RX FIFO and TX FIFO Thresholds
    0x57,  # SYNC1         Sync Word, High Byte
    0x43,  # SYNC0         Sync Word, Low Byte
    0x3E,  # PKTLEN        Packet Length
    0x0E,  # PKTCTRL1      Packet Automation Control
    0x45,  # PKTCTRL0      Packet Automation Control
    0xFF,  # ADDR          Device Address
    0x00,  # CHANNR        Channel Number
    0x08,  # FSCTRL1       Frequency Synthesizer Control
    0x00,  # FSCTRL0       Frequency Synthesizer Control
    0x21,  # FREQ2         Frequency Control Word, High Byte
    0x65,  # FREQ1         Frequency Control Word, Middle Byte
    0x6A,  # FREQ0         Frequency Control Word, Low Byte
    0x5B,  # MDMCFG4       Modem Configuration
    0xF8,  # MDMCFG3       Modem Configuration
    0x13,  # MDMCFG2       Modem Configuration
    0xA0,  # MDMCFG1       Modem Configuration
    0xF8,  # MDMCFG0       Modem Configuration
    0x47,  # DEVIATN       Modem Deviation Setting
    0x07,  # MCSM2         Main Radio Control State Machine Configuration
    0x0C,  # MCSM1         Main Radio Control State Machine Configuration
    0x18,  # MCSM0         Main Radio Control State Machine Configuration
    0x1D,  # FOCCFG        Frequency Offset Compensation Configuration
    0x1C,  # BSCFG         Bit Synchronization Configuration
    0xC7,  # AGCCTRL2      AGC Control
    0x00,  # AGCCTRL1      AGC Control
    0xB2,  # AGCCTRL0      AGC Control
    0x02,  # WOREVT1       High Byte Event0 Timeout
    0x26,  # WOREVT0       Low Byte Event0 Timeout
    0x09,  # WORCTRL       Wake On Radio Control
    0xB6,  # FREND1        Front End RX Configuration
    0x17,  # FREND0        Front End TX Configuration
    0xEA,  # FSCAL3        Frequency Synthesizer Calibration
    0x0A,  # FSCAL2        Frequency Synthesizer Calibration
    0x00,  # FSCAL1        Frequency Synthesizer Calibration
    0x11,  # FSCAL0        Frequency Synthesizer Calibration
    0x41,  # RCCTRL1       RC Oscillator Configuration
    0x00,  # RCCTRL0       RC Oscillator Configuration
    0x59,  # FSTEST        Frequency Synthesizer Calibration Control,
    0x7F,  # PTEST         Production Test
    0x3F,  # AGCTEST       AGC Test
    0x81,  # TEST2         Various Test Settings
    0x3F,  # TEST1         Various Test Settings
    0x0B   # TEST0         Various Test Settings
]}
