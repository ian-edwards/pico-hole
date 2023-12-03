import led
import wifi
import secrets
import log
import time

log.message('starting...')
led.status_active()
wifi.connect(secrets.wifi_name, secrets.wifi_password)
time.sleep(2)
led.status_error()