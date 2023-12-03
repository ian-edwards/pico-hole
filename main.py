import led
import wifi
import dns
import settings
import log
import error

led.status_normal()
wifi.connect(settings.WIFI_NAME, settings.WIFI_PASSWORD, connect_timeout = 10_000)
if wifi.ok():
    log.message("WiFi OK:" + wifi.status()[0])
    socket = dns.create_socket()
    while True:
        (data, address) = socket.recvfrom(512)
        print(data)
else:
    error.status("WiFi Error")