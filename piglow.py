#####################################################
## Python module to control the PiGlow by Pimoroni ##
##                                                 ##
## Written by Jason - @Boeeerb  -  v0.5  17/08/13  ##
##            jase@boeeerb.co.uk                   ##
#####################################################
##
## v0.5 - Add RPI VER 3 for model B+         - 26/08/14
## v0.4 - Auto detect Raspberry Pi revision  - 17/08/13
## v0.3 - Added fix from topshed             - 17/08/13
## v0.2 - Code cleanup by iiSeymour          - 15/08/13
## v0.1 - Initial release                    - 15/08/13
##

from smbus import SMBus
import RPi.GPIO as rpi

bus = 0

class PiGlow:

    def __init__(self):
        if rpi.RPI_REVISION == 1:
            i2c_bus = 0
        elif rpi.RPI_REVISION == 2:
            i2c_bus = 1
        elif rpi.RPI_REVISION == 3:
            i2c_bus = 1
        else:
            print "Unable to determine Raspberry Pi revision."
            exit

        self.bus = SMBus(i2c_bus)
        self.bus.write_i2c_block_data(0x54, 0x00, [0x01])
        self.bus.write_byte_data(0x54, 0x13, 0xFF)
        self.bus.write_byte_data(0x54, 0x14, 0xFF)
        self.bus.write_byte_data(0x54, 0x15, 0xFF)

    def white(self, value):
        self.bus.write_byte_data(0x54, 0x0A, value)
        self.bus.write_byte_data(0x54, 0x0B, value)
        self.bus.write_byte_data(0x54, 0x0D, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def blue(self, value):
        self.bus.write_byte_data(0x54, 0x05, value)
        self.bus.write_byte_data(0x54, 0x0C, value)
        self.bus.write_byte_data(0x54, 0x0F, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def green(self, value):
        self.bus.write_byte_data(0x54, 0x06, value)
        self.bus.write_byte_data(0x54, 0x04, value)
        self.bus.write_byte_data(0x54, 0x0E, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def yellow(self, value):
        self.bus.write_byte_data(0x54, 0x09, value)
        self.bus.write_byte_data(0x54, 0x03, value)
        self.bus.write_byte_data(0x54, 0x10, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def orange(self, value):
        self.bus.write_byte_data(0x54, 0x08, value)
        self.bus.write_byte_data(0x54, 0x02, value)
        self.bus.write_byte_data(0x54, 0x11, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def red(self, value):
        self.bus.write_byte_data(0x54, 0x07, value)
        self.bus.write_byte_data(0x54, 0x01, value)
        self.bus.write_byte_data(0x54, 0x12, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def all(self, value):
        v = value
        self.bus.write_i2c_block_data(
            0x54, 0x01, [v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v, v])
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def arm(self, arm, value):
        if arm == 1:
            self.bus.write_byte_data(0x54, 0x07, value)
            self.bus.write_byte_data(0x54, 0x08, value)
            self.bus.write_byte_data(0x54, 0x09, value)
            self.bus.write_byte_data(0x54, 0x06, value)
            self.bus.write_byte_data(0x54, 0x05, value)
            self.bus.write_byte_data(0x54, 0x0A, value)
            self.bus.write_byte_data(0x54, 0x16, 0xFF)
        elif arm == 2:
            self.bus.write_byte_data(0x54, 0x0B, value)
            self.bus.write_byte_data(0x54, 0x0C, value)
            self.bus.write_byte_data(0x54, 0x0E, value)
            self.bus.write_byte_data(0x54, 0x10, value)
            self.bus.write_byte_data(0x54, 0x11, value)
            self.bus.write_byte_data(0x54, 0x12, value)
            self.bus.write_byte_data(0x54, 0x16, 0xFF)
        elif arm == 3:
            self.bus.write_byte_data(0x54, 0x01, value)
            self.bus.write_byte_data(0x54, 0x02, value)
            self.bus.write_byte_data(0x54, 0x03, value)
            self.bus.write_byte_data(0x54, 0x04, value)
            self.bus.write_byte_data(0x54, 0x0F, value)
            self.bus.write_byte_data(0x54, 0x0D, value)
            self.bus.write_byte_data(0x54, 0x16, 0xFF)
        else:
            print "Unknown number, expected only 1, 2 or 3"

    def arm1(self, value):
        self.bus.write_byte_data(0x54, 0x07, value)
        self.bus.write_byte_data(0x54, 0x08, value)
        self.bus.write_byte_data(0x54, 0x09, value)
        self.bus.write_byte_data(0x54, 0x06, value)
        self.bus.write_byte_data(0x54, 0x05, value)
        self.bus.write_byte_data(0x54, 0x0A, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def arm2(self, value):
        self.bus.write_byte_data(0x54, 0x0B, value)
        self.bus.write_byte_data(0x54, 0x0C, value)
        self.bus.write_byte_data(0x54, 0x0E, value)
        self.bus.write_byte_data(0x54, 0x10, value)
        self.bus.write_byte_data(0x54, 0x11, value)
        self.bus.write_byte_data(0x54, 0x12, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def arm3(self, value):
        self.bus.write_byte_data(0x54, 0x01, value)
        self.bus.write_byte_data(0x54, 0x02, value)
        self.bus.write_byte_data(0x54, 0x03, value)
        self.bus.write_byte_data(0x54, 0x04, value)
        self.bus.write_byte_data(0x54, 0x0F, value)
        self.bus.write_byte_data(0x54, 0x0D, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def colour(self, colour, value):
        if colour == 1 or colour == "white":
            self.bus.write_byte_data(0x54, 0x0A, value)
            self.bus.write_byte_data(0x54, 0x0B, value)
            self.bus.write_byte_data(0x54, 0x0D, value)
            self.bus.write_byte_data(0x54, 0x16, 0xFF)

        elif colour == 2 or colour == "blue":
            self.bus.write_byte_data(0x54, 0x05, value)
            self.bus.write_byte_data(0x54, 0x0C, value)
            self.bus.write_byte_data(0x54, 0x0F, value)
            self.bus.write_byte_data(0x54, 0x16, 0xFF)

        elif colour == 3 or colour == "green":
            self.bus.write_byte_data(0x54, 0x06, value)
            self.bus.write_byte_data(0x54, 0x04, value)
            self.bus.write_byte_data(0x54, 0x0E, value)
            self.bus.write_byte_data(0x54, 0x16, 0xFF)

        elif colour == 4 or colour == "yellow":
            self.bus.write_byte_data(0x54, 0x09, value)
            self.bus.write_byte_data(0x54, 0x03, value)
            self.bus.write_byte_data(0x54, 0x10, value)
            self.bus.write_byte_data(0x54, 0x16, 0xFF)

        elif colour == 5 or colour == "orange":
            self.bus.write_byte_data(0x54, 0x08, value)
            self.bus.write_byte_data(0x54, 0x02, value)
            self.bus.write_byte_data(0x54, 0x11, value)
            self.bus.write_byte_data(0x54, 0x16, 0xFF)
        elif colour == 6 or colour == "red":
            self.bus.write_byte_data(0x54, 0x07, value)
            self.bus.write_byte_data(0x54, 0x01, value)
            self.bus.write_byte_data(0x54, 0x12, value)
            self.bus.write_byte_data(0x54, 0x16, 0xFF)
        else:
            print "Only colours 1 - 6 or color names are allowed"

    def led(self, led, value):
        leds = [
            "0x00", "0x07", "0x08", "0x09", "0x06", "0x05", "0x0A", "0x12", "0x11",
            "0x10", "0x0E", "0x0C", "0x0B", "0x01", "0x02", "0x03", "0x04", "0x0F", "0x0D"]
        self.bus.write_byte_data(0x54, int(leds[led], 16), value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led1(self, value):
        self.bus.write_byte_data(0x54, 0x07, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led2(self, value):
        self.bus.write_byte_data(0x54, 0x08, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led3(self, value):
        self.bus.write_byte_data(0x54, 0x09, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led4(self, value):
        self.bus.write_byte_data(0x54, 0x06, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led5(self, value):
        self.bus.write_byte_data(0x54, 0x05, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led6(self, value):
        self.bus.write_byte_data(0x54, 0x0A, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led7(self, value):
        self.bus.write_byte_data(0x54, 0x12, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led8(self, value):
        self.bus.write_byte_data(0x54, 0x11, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led9(self, value):
        self.bus.write_byte_data(0x54, 0x10, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led10(self, value):
        self.bus.write_byte_data(0x54, 0x0E, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led11(self, value):
        self.bus.write_byte_data(0x54, 0x0C, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led12(self, value):
        self.bus.write_byte_data(0x54, 0x0B, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led13(self, value):
        self.bus.write_byte_data(0x54, 0x01, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led14(self, value):
        self.bus.write_byte_data(0x54, 0x02, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led15(self, value):
        self.bus.write_byte_data(0x54, 0x03, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led16(self, value):
        self.bus.write_byte_data(0x54, 0x04, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led17(self, value):
        self.bus.write_byte_data(0x54, 0x0F, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)

    def led18(self, value):
        self.bus.write_byte_data(0x54, 0x0D, value)
        self.bus.write_byte_data(0x54, 0x16, 0xFF)
