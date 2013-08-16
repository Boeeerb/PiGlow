##################################################
## Switch each colour on in sequence on and off ##
##                                              ##
## Example by Jason - @Boeeerb                  ##
##################################################

from piglow import PiGlow
from time import sleep

piglow = PiGlow(1)
val = 20
colour = 1

while True:
    if colour == 19:
        colour = 1
        if val == 20:
            val = 0
        else:
            val = 20

    piglow.led(colour, val)
    sleep(0.2)

    colour = colour + 1
