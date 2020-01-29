# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 19:41:22 2020

@author: Administrator
"""

import socket

def client_program():
    target_ip="11.11.29.200"
    target_port=2623
    
    client_socket = socket.socket()
    client_socket.connect((target_ip, target_port))
    message = input(" -> ")
    
    while message.lower().strip() != 'bye' :
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        
        print('received from server : ' +data)
        
        message = input(" -> ")
        
    client_socket.close()
    
if __name__ == '__main__' :
    client_program()