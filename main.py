import net
import log

def raise_exception(error_message):
    raise Exception(error_message)

log.msg("Pico Hole Initializing...")
net.connect_wifi(wifi_name="Your WiFi Name", wifi_password="Your WiFi Password", wifi_timeout=5_000) or raise_exception("Wifi Error!")

server = net.create_socket(socket_port=80) or raise_exception("Socket Error!")

client, address = server.accept()
request = client.recv(1024)
print(request)
         
