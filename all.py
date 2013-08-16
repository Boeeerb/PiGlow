##################################################
## Test the brightness of all the LEDs together ##
##                                              ##
## Example by Jason - @Boeeerb                  ##
##################################################

from piglow import PiGlow
from time import sleep

piglow = PiGlow(1)

while True:
    count = range(0, 256, +1)
    for item in count:
        if item < 256:
            piglow.all(item)
            sleep(0.01)
        if item == 256:
            break
    count = range(255, 0, -1)
    print "Brightest"
    for item in count:
        if item > 0:
            piglow.all(item)
            sleep(0.01)
        if item == 0:
            piglow.all(0)
            break
    print "Fin"
    break
