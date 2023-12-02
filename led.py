import machine
import time
from status import Status
    
def led_status(status_code):
    machine_led = machine.Pin("LED", machine.Pin.OUT)
    if status_code == Status.OK():
        machine_led.on()
    else:        
        while (True):
            machine_led.on()
            time.sleep(0.5)
            machine_led.off()
            time.sleep(0.5)
