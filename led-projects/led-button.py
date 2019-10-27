'''
led-button.py
-------------
Switch a led on and off using a push-button for a given period.

Required:
- LED
- Resistor (> ~220 Ohm)
- Push-button

Note: The exact value of resistor needed depends on the LED we are using, but 330 Ohm works for most common LEDS. 
'''

# Import necessary modules
from gpiozero import LED, Button
from time import sleep 

# Choose pin
led_pin = 17
button_pin = 2

# GPIO pin
led = LED(led_pin)

# Button
button = Button(button_pin)

# Wait for press
button.wait_for_press()
print("On")

# Switch the led on
led.on()

# Wait for 5 sec
sleep(5)

# Swiitch the led off
led.off()

