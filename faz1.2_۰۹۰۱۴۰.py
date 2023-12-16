# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 19:35:21 2023

@author: Hedyeloo
"""
# مهدی هدیه لو 98213218
import socket 
def scan_ports(host,start_port,end_port):
    open_ports = []
    for port in range(start_port,end_port+1):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host,port))
        if result ==0:
            open_ports.append(port)
        sock.close()
        
    return open_ports
host = input(print("pleas enter the host:"))

start_port = 1
end_port = 1024
open_ports = scan_ports(host,start_port,end_port)
if open_ports:
    print(f"the follwing ports ar open on {host}: {open_ports}")
    print(f" no open ports found on {host}")