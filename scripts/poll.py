
#Licensed under the MIT licence 
#To end the Programme use "C+Ctrl" at the same time. 

#pretty obvious, but you'll want these dependencies to be installed for this script to work

# This imports the Raspberry Pi's GPIO library but as GPIO so we don't need to be repeating it.
import RPi.GPIO as GPIO

import json
import os
#This is used to sleep the code a the end.
import time
import json
#Requests is the ONE that is need to be installed with "sudo apt-get install python-requests" this lets us to grab and interpret PHP
import requests

def cls():
    os.system(['clear','cls'][os.name == 'nt'])
	
# #Uncomment this is you don't want to get the GPIO warning. This is useful if you changing things around constantly and are ending the code.
# #GPIO.setwarnings(False)

# DEBUG = 1

# #this defines the pins for each ONE
# ONE = 23
# TWO = 24
# THREE = 25
GPIO.cleanup()
# #sets the mode for the pin out
GPIO.setmode(GPIO.BOARD)

# #defines if the pins are inputs or out puts
# GPIO.setup(ONE, GPIO.OUT)
# GPIO.setup(TWO, GPIO.OUT)
# GPIO.setup(THREE, GPIO.OUT)
available_pin_mapping = {}
available_pin_mapping["4"] = 7
available_pin_mapping["17"] = 11
available_pin_mapping["27"] = 13
available_pin_mapping["22"] = 15
available_pin_mapping["5"] = 29
available_pin_mapping["6"] = 31
available_pin_mapping["0"] = 11
for gpio_pin in available_pin_mapping: 
    GPIO.setup(available_pin_mapping[gpio_pin],GPIO.OUT)

# #replace the http://YourWebsite.com/test.php with where your test.php is located.
response = requests.get('http://localhost:8000/app/api/')

#replace the http://YourWebsite.com/test.php with where your test.php is located.
while response.text != 'exit':
    response = requests.get('http://localhost:8000/app/api/')
    if response.status_code != 200: 
        time.sleep(5)
        continue
    content = json.loads(response.text)
    print(content)
    for gpio_setting in content: 
        pin_number = content[gpio_setting]["GPIO_Pin"]
        toggle_on = content[gpio_setting]["toggle_on"]
        print(pin_number,toggle_on)
        if pin_number in available_pin_mapping: 
            GPIO.output(available_pin_mapping[pin_number],toggle_on)
    #This says ONE is the first digit TWO is the second and THREE is the last 




#This can be removed but this time is to stop the web server from being overloaded with requests.
    time.sleep(0.15)
