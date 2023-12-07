from network import WLAN, STA_IF
from time import ticks_ms, ticks_add, ticks_diff, sleep

def raise_exception(error_message): raise Exception(error_message)

def connect_wifi(wifi_name, wifi_password, wifi_timeout):
    wifi = WLAN(STA_IF)
    wifi.active(True)
    wifi.connect(wifi_name, wifi_password)
    deadline = ticks_add(ticks_ms(), max(wifi_timeout, 0))
    while (wifi.isconnected() == False and ticks_diff(deadline, ticks_ms()) > 0):
        sleep(0.5)
    return wifi.isconnected()

connect_wifi(wifi_name="Your WiFi Name", wifi_password="Your WiFi Password", wifi_timeout=5_000) or raise_exception("Wifi Error!")

print("WiFi OK!")