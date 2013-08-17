##################################################
## Switch each colour on in sequence on and off ##
##                                              ##
## Example by Jason - @Boeeerb                  ##
##################################################

from piglow import PiGlow
from time import sleep

piglow = PiGlow()

while True:
    piglow.white(10)
    sleep(0.1)
    piglow.blue(10)
    sleep(0.1)
    piglow.green(10)
    sleep(0.1)
    piglow.yellow(10)
    sleep(0.1)
    piglow.orange(10)
    sleep(0.1)
    piglow.red(10)
    sleep(0.1)
    piglow.red(0)
    sleep(0.1)
    piglow.orange(0)
    sleep(0.1)
    piglow.yellow(0)
    sleep(0.1)
    piglow.green(0)
    sleep(0.1)
    piglow.blue(0)
    sleep(0.1)
    piglow.white(0)
    sleep(0.1)
