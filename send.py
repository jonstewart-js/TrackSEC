from microbit import *
import radio
import time

#radio channel is set to 185, power range 1
radio.on
radio.config(group=185, power=7)

while True:
    radio.send("signal")
    time.sleep(0.1)
