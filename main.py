import led
import wifi
import settings
import log
import time

led.status_normal()
wifi.connect(settings.WIFI_NAME, settings.WIFI_PASSWORD, connect_timeout = 10_000)
time.sleep(2)
led.status_error()