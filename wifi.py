import network
import time

def ok():
    return network.WLAN(network.STA_IF).isconnected()

def status():
    return network.WLAN(network.STA_IF).ifconfig()

def connect(wifi_name, wifi_password, connect_timeout, poll_interval = 0.5):
    deadline = time.ticks_add(time.ticks_ms(), connect_timeout)
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(wifi_name, wifi_password)
    while (wifi.isconnected() == False and time.ticks_diff(deadline, time.ticks_ms()) > 0):
        time.sleep(poll_interval)