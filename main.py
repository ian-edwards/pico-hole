from wifi import connect_wifi
from server import create_server
from error import raise_exception

connect_wifi(wifi_name="Your WiFi Name", wifi_password="Your WiFi Password", wifi_timeout=5_000) or raise_exception("Wifi Error!")

server = create_server(server_port=8000) or raise_exception("Server Error!")

server.listen(0)
print("Listening...")
client_socket, client_address = server.accept()
print("Accepted...")
while True:
    request = client_socket.recv(1024)
    request = request.decode("utf-8")
    if request.lower() == "close":
        client_socket.send("closed".encode("utf-8"))
        break

print("Received")
         
