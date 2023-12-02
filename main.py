from led import led_status_ok, led_status_error
from wifi import wifi_connect
from secrets import wifi_name, wifi_password
import time

led_status_ok()
wifi_connect(wifi_name, wifi_password)
time.sleep(2)
led_status_error(123)