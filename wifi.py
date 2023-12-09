from network import WLAN, STA_IF
from time import ticks_ms, ticks_add, ticks_diff, sleep

def connect_wifi(wifi_name, wifi_password, wifi_timeout):
    print("WiFi Initializing...")
    wifi = WLAN(STA_IF)
    wifi.active(True)
    print(f"WiFi Name '{wifi_name}'")
    print(f"WiFi Password {'*' * len(wifi_password)}")
    wifi.connect(wifi_name, wifi_password)
    deadline = ticks_add(ticks_ms(), max(wifi_timeout, 0))
    while (wifi.isconnected() == False and ticks_diff(deadline, ticks_ms()) > 0):
        print("WiFi Connecting...")
        sleep(1)
    if wifi.isconnected():
        print("WiFi Connected!")
        (ip_address, subnet_mask, gateway_address, dns_address) = wifi.ifconfig()
        print(f"Wifi IP Address {ip_address}")
        print(f"Wifi Subnet Mask {subnet_mask}")
        print(f"Wifi Gateway Address {gateway_address}")
        print(f"Wifi DNS Address {dns_address}")
        return True
    else:
        print(f"WiFi Connection Failed!")
        print(f"Wifi Error Code {wifi.status()}")
        return False