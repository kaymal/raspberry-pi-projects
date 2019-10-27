'''
Switch the led on and off for a given time period.
'''

# Import necessary modules
from gpiozero import LED
from time import sleep

# Create seconds
sec =  10

# Choose pin
pin = 17

# GPIO pin
led = LED(pin)

for i in range(sec):

    # Switch the led on
    led.on()
    
    # Wait for 1 sec
    sleep(1)

    # Swiitch the led off
    led.off()

    # Wait for 1 sec
    sleep(1)
    
    # Increment i
    i = i + 1