import socket
from socket import create_connection



def scanner(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Hard coded ssh example
    result = s.connect((ip, 22))

    if result == 0:
        return True
    else:
        return False




