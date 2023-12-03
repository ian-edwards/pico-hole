import socket

def create_socket():
    address = '127.0.0.1'
    port = 53
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((address, port))
    return sock