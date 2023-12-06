from led import led_normal
from wifi import wifi_connect
from settings import WIFI_NAME, WIFI_PASSWORD
from error import on_error
import dns

led_normal()
wifi_connect(WIFI_NAME, WIFI_PASSWORD, lambda: on_error("WiFi Error"))
print("WiFi OK!")