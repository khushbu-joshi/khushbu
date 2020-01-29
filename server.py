# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 20:15:29 2020

@author: Administrator
"""

import socket

def server_program():
    target_ip="11.11.29.200"
    target_port=2623
    
    server_socket = socket.socket()
    server_socket.bind((target_ip, target_port))
    
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("connection from: "+ str(address))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())
        
    conn.close()
    
if __name__== '__main__':
    server_program()