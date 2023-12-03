import led
import log

def status(message):
    log.message(message)
    led.status_error()