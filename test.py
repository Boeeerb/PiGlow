######################################################
## Set each colour to a brightness of your choosing ##
##                                                  ##
##  Example by Jason - @Boeeerb                     ##
######################################################

from piglow import PiGlow

piglow = PiGlow(1)

val = input("White: ")
piglow.white(val)

val = input("Blue: ")
piglow.blue(val)

val = input("Green: ")
piglow.green(val)

val = input("Yellow: ")
piglow.yellow(val)

val = input("Orange: ")
piglow.orange(val)

val = input("Red: ")
piglow.red(val)

val = input("All: ")
piglow.all(val)
