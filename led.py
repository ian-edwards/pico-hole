import machine
import time

def led_status_ok():
    machine.Pin("LED", machine.Pin.OUT).on()
    
def led_status_error(error_code):
    led = machine.Pin("LED", machine.Pin.OUT)
    led.off()
    while (True):
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
