Here is a small Python module for the PiGlow addon by Pimoroni, it will let you flex the LED muscles of this fantastic addon.

File list:

 - piglow.py - Python module you'll import into your script
 - all.py - This will increase then decrease all the LEDs together
 - cycle.py - This will cycle the colours together from center to the end back to the center
 - indiv.py - Quickly increase and decrease the LEDs independantly
 - test.py - You choose the brightness of each LED colour group, to see how it will look
 - arm.py - Cycle each of the PiGlow arms, showing both methods
 - cycle2.py - Switch each individual colour using the piglow.colour method
 - indiv2.py - Switch each LED on individually in a loop cycle
 - cpu.py - Show your current CPU usage on the PiGlow - Requires psutils:
             
    sudo apt-get install python-psutils

The functions of piglow are:


    from piglow import PiGlow

    piglow = PiGlow([0/1])

    piglow.colour([1-6],[0-255])    # 1= White, 2= Blue, 3= Green, 4= Yellow, 5= Orange, 6= Red

    piglow.white([0-255])           # Control all the white LEDs

    piglow.blue([0-255])            # Control all the blue LEDs

    piglow.green([0-255])           # Control all the green LEDs

    piglow.yellow([0-255])          # Control all the yellow LEDs

    piglow.orange([0-255])          # Control all the orange LEDs

    piglow.red([0-255])             # Control all the red LEDs

    piglow.all([0-255])             # Control all LEDs together

    piglow.led([1-18],[0-255])      # Control an individual LED by number

    piglow.led1-led18([0-255])      # Control an individual LED by function

    piglow.arm([1-3],[0-255])       # Control an arm of LEDs by number

    piglow.arm1([0-255])            # Control the top arm (with PiGlow logo at the top)

    piglow.arm2([0-255])            # Control the right arm (with PiGlow logo at the top)

    piglow.arm3([0-255])            # Control the left arm (with PiGlow logo at the top)


All colours are from 0 (off) to 255 (super duper eye numbing bright!)


Enjoy!

Jason

http://www.boeeerb.co.uk

Buy from http://shop.pimoroni.com/collections/accessories/products/piglow
