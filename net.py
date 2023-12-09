import network
import socket
import time
import log

def connect_wifi(wifi_name, wifi_password, wifi_timeout):
    log.msg("WiFi Initializing...")
    log.msg(f"WiFi Name '{wifi_name}'")
    log.msg(f"WiFi Password {'*' * len(wifi_password)}")
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)
    wifi.connect(wifi_name, wifi_password)
    deadline = time.ticks_add(time.ticks_ms(), max(wifi_timeout, 0))
    while (wifi.isconnected() == False and time.ticks_diff(deadline, time.ticks_ms()) > 0):
        log.msg("WiFi Connecting...")
        time.sleep(1)
    if wifi.isconnected():
        log.msg("OK! WiFi Connected!")
        (ip_address, subnet_mask, gateway_address, dns_address) = wifi.ifconfig()
        log.msg(f"Wifi IP Address {ip_address}")
        log.msg(f"Wifi Subnet Mask {subnet_mask}")
        log.msg(f"Wifi Gateway Address {gateway_address}")
        log.msg(f"Wifi DNS Address {dns_address}")
        return True
    else:
        log.msg("ERROR! WiFi Connection Failed!")
        log.msg(f"ERROR! Wifi Error Code {wifi.status()}")
        return False

def create_socket(socket_port):
    log.msg("Creating Socket...")
    log.msg(f"Socket Bind Port {socket_port}")
    address = socket.getaddrinfo('0.0.0.0', socket_port)[0][-1]
    server = socket.socket()
    server.bind(address)
    server.listen(1)
    log.msg("OK! Socket Listening!")
    return server