import network
import time
import log

def connect(wifi_name, wifi_password):
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(wifi_name, wifi_password)
    log.message("connecting wifi...")
    while wifi.isconnected() == False:
        sleep(1)
    log.message("wifi connected!")