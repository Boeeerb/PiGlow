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
    sleep(random.uniform(0,1))
    return random.randint(0,255)

while True:
    piglow.yellow(random_brightness())
    piglow.orange(random_brightness())
    piglow.red(random_brightness())
