from network import WLAN, STA_IF
from time import ticks_ms, ticks_add, ticks_diff, sleep
from settings import WIFI_POLL, WIFI_TIMEOUT

def wifi_connect(wifi_name, wifi_password, on_error):
    deadline = ticks_add(ticks_ms(), WIFI_TIMEOUT)
    wifi = WLAN(STA_IF)
    wifi.active(True)
    wifi.connect(wifi_name, wifi_password)
    while (wifi.isconnected() == False and ticks_diff(deadline, ticks_ms()) > 0):
        sleep(WIFI_POLL)
    if wifi.isconnected() == False and on_error is not None:
        on_error()