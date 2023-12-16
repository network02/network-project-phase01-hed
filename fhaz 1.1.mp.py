# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:35:25 2023

@author: Hedyeloo
"""

import socket
 
def is_host_online(host,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((host,port))
    sock.close()
    if result ==0:
        print(f'{host}:{port}  is reachable')
        
    else:
        print(f'{host}:{port}  is not reachable')
        
#host=input(print("pleas enter the host:"))
#port=input(print("pleas enter the port:")) 
host=127.0.0.1
port=80
is_host_online(host,port)       