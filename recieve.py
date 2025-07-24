from microbit import *
import radio
import time
import music

#radio channel is set to 185, power range 
radio.on()
radio.config(group=185, power = 7)

debounce = False

while True:
    rssi = radio.receive_full()
    if rssi:
        message, signal_strength, _ = rssi
        if signal_strength > -45: # ~8 feet
            display.on()
            display.show(Image.SQUARE)
            time.sleep(0.2)
            display.off()
            time.sleep(0.2)
