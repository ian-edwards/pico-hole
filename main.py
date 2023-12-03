import led
import wifi
import settings
import log
import error

led.status_normal()
wifi.connect(settings.WIFI_NAME, settings.WIFI_PASSWORD, connect_timeout = 10_000)
if wifi.is_connected():
    log.message("WiFi OK")
else:
    error.status("WiFi Error")