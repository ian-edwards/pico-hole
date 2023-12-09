from socket import socket, AF_INET, SOCK_STREAM

def create_server(server_port):
    print("Server Initializing...")
    server = socket(AF_INET, SOCK_STREAM)
    print(f"Server Port {server_port}")
    server.bind(("127.0.0.1", server_port))
    return server