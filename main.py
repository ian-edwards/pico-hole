from machine import Pin
from network import WLAN, STA_IF
from time import ticks_ms, ticks_add, ticks_diff

def raise_exception(error_message): raise Exception(error_message)

def connect_wifi(wifi_name, wifi_password, wifi_timeout):
    deadline = ticks_add(ticks_ms(), wifi_timeout)
    wifi = WLAN(STA_IF)
    wifi.active(True)
    wifi.connect(wifi_name, wifi_password)
    while (wifi.isconnected() == False and ticks_diff(deadline, ticks_ms()) > 0):
        pass
    return wifi.isconnected()

Pin("LED", machine.Pin.OUT).on()
connect_wifi(wifi_name="Your WiFi Name", wifi_password="Your WiFi Password", wifi_timeout=5_000) or raise_exception("Wifi Error!")

print("WiFi OK!")