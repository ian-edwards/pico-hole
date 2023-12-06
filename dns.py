import usocket

def create_socket():
    sock = usocket.socket(usocket.AF_INET, usocket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 80))
    sock.listen(9)
    print(sock)
    return sock