import machine
import time
    
def status_normal():
    machine.Pin("LED", machine.Pin.OUT).on()
    
def status_error():
    led = machine.Pin("LED", machine.Pin.OUT)
    while (True):
        led.toggle()
        time.sleep(0.5)