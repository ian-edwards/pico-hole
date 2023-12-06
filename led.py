from machine import Pin
from time import sleep
    
def led_normal():
    Pin("LED", Pin.OUT).on()
    
def led_error():
    led = Pin("LED", Pin.OUT)
    while (True):
        led.toggle()
        sleep(0.5)