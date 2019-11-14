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
red_pin = 17
orange_pin = 16
green_pin = 21
button_pin = 2
buzzer_pin = 18

# GPIO pin
led_red = LED(red_pin)
led_orange = LED(orange_pin)
led_green = LED(green_pin)

# Button
button = Button(button_pin)

# Buzzer
buzzer = Buzzer(buzzer_pin)

while True:

    if button.is_pressed:
        
        print("On")

        # Buzzer on
        buzzer.on()

        # Orange on and off
        led_orange.on()
        sleep(0.5)
        led_orange.off()
        
        # Green on
        led_green.on()
        
        # Wait for release
        button.wait_for_release()
        
        # Green off
        led_green.off()
        
    else:
        # Buzzer off
        buzzer.off()
        
        # Orange on and off
        led_orange.on()
        sleep(0.5)
        led_orange.off()
        
        # Red light on
        led_red.on()
        
        # Wait for press
        button.wait_for_press()
        
        # Red off
        led_red.off()

        print("Off")
