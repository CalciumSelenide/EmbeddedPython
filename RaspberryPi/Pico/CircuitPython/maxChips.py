# ====================================================================================
# Developed by CalciumSelenide
# Last Edit: 2024/05/24
# ====================================================================================
# CircuitPython for boards like the RPi Pico interfacing with maxim integrated chips.

# +++++++++++++++++++++++ Example Boards for Rapid Development +++++++++++++++++++++++
# https://www.adafruit.com/product/269
# https://www.sparkfun.com/products/13266

import digitalio
import struct
import board
import busio

class MAX31855:
    def __init__(self, SRCLK:board , CHPSL:board , CHPTX:board):
        # MAX31855 Thermocouple Chip Object
        # SRCLK - Serial Clock
        # CHPSL - Chip Select
        # CHPTX - Chip TX (data)
        self.SRCLK = SRCLK
        self.CHPSL = CHPSL
        self.CHPTX = CHPTX

        # Setting up specific pins for use
        # CHiP SeLect
        self.CHPSL = digitalio.DigitalInOut(self.CHPSL)
        self.CHPSL.direction = digitalio.Direction.OUTPUT
        self.CHPSL.value = True

        # SPI parameters
        self.spiBaud = 5000000
        self.spiPhase = 0
        self.spiPolarity = 0

        # Declaring the SPI bus
        self.spi = busio.SPI(clock=self.SRCLK, MISO=self.CHPTX)

    def read(self):
        # Make sure you are the only one reading the bus ...
        while not self.spi.try_lock():
            pass

        # ... reconfigure after every lock/unlock ...
        self.spi.configure(baudrate=self.spiBaud, phase=self.spiPhase, polarity=self.spiPolarity)

        # ... tell our CHPSL we are ready for data and pack it ...
        self.CHPSL.value = False
        packetData = bytearray(4)
        self.spi.readinto(packetData)
        self.CHPSL.value = True
        self.spi.unlock()

        # ... now return our data!
        return packetData

    @property
    def temperatures(self):
        # Read the data from the MAX31855 chip ...
        result = self.read()

        # ... check for and handle errors ...
        if result[3] & 0x01:
            return "ERROR: Thermocouple not connected"
        elif result[3] & 0x02:
            return "ERROR: Short-Circuit to GND"
        elif result[3] & 0x04:
            return "ERROR: Short-Circuit to PWR"
        elif result[1] & 0x01:
            return "ERROR: Faulty read"

        # ... calculate the sensed and internal reference temperatures
        temperature, reference = struct.unpack(">hh", result)
        temperature >>= 2
        reference >>= 4

        return ((temperature / 4), (reference * 0.0625))

if __name__ == "__main__":
    # This is a compilation test for an RP2040 based board
    data = board.GP16
    chipSelect = board.GP17
    serialClock = board.GP18

    maxChip = MAX31855(serialClock, chipSelect, data)
    print(str(maxChip.temperatures))
    print("Compilation test complete")
