##########################################################
## Show your current CPU usage on your PiGlow!          ##
##                                                      ##
## Requires psutil - sudo apt-get install python-psutil ##
##                                                      ##
## Example by Jason - @Boeeerb                          ##
##########################################################

from piglow import PiGlow
from time import sleep
import psutil

piglow = PiGlow()

while True:

    cpu = psutil.cpu_percent()
    piglow.all(0)

    if cpu < 5:
        piglow.white(20)
    elif cpu < 20:
        piglow.white(20)
        piglow.blue(20)
    elif cpu < 40:
        piglow.white(20)
        piglow.blue(20)
        piglow.green(20)
    elif cpu < 60:
        piglow.white(20)
        piglow.blue(20)
        piglow.green(20)
        piglow.yellow(20)
    elif cpu < 80:
        piglow.white(20)
        piglow.blue(20)
        piglow.green(20)
        piglow.yellow(20)
        piglow.orange(20)
    else:
        piglow.all(20)
    sleep(0.2)
