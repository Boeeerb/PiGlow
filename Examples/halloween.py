##################################################
## Switch only yellow, orange and red to random ##
## brightness                                   ##
## Example by tng - @TommyBobbins               ##
##################################################

from piglow import PiGlow
from time import sleep
import random

piglow = PiGlow()

def random_brightness():
     return random.randint(0,255)

while True:
    piglow.yellow(random_brightness())
    sleep(random.random())
    piglow.orange(random_brightness())
    sleep(random.random())
    piglow.red(random_brightness())
    sleep(random.random())
