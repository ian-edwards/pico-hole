import network
import time

def wifi_connect(wifi_name, wifi_password):
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(wifi_name, wifi_password)
    while wifi.isconnected() == False:
        sleep(1)
    print(wifi.ifconfig())