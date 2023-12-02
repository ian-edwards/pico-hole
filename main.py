import machine
led = machine.Pin("LED", machine.Pin.OUT)
led.off()
led.on()

print('hello world!')