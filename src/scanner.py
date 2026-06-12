import socket
from dataclasses import dataclass
from socket import create_connection
from concurrent.futures import ThreadPoolExecutor
import time






def scanner(ip):

    results = []
    for i in range(1000):
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       s.settimeout(0.5)


       if s.connect_ex((ip, i)) == 0:
           results.append({"port": i, "status": "open"})
       else:
           results.append({"port": i, "status": "closed"})
       s.close()
       if i % 10 == 0:
           print("Progess: " + str((i/1000)*100) + "% done")





    return results




