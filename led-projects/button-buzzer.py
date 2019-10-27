'''
led-button.py
-------------
Control a buzzer and a led using a push-button for a given period.

Required:
- LED
- Resistor (> ~220 Ohm)
- Push-button
- Buzzer
'''

# Import necessary modules
from gpiozero import LED, Button, Buzzer
from time import sleep 

# Choose pin
led_pin = 17
button_pin = 2
buzzer_pin = 18

# GPIO pin
led = LED(led_pin)

# Button
button = Button(button_pin)

# Buzzer
buzzer = Buzzer(buzzer_pin)

while True:

    # Wait for press
    if button.is_pressed:
        print("On")

        # Switch the led on
        led.on()

        # Buzzer on
        buzzer.on()
    else:
        # Switch the led off
        led.off()

        # Buzzer ff
        buzzer.off()

        print("Off")
