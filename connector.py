#!/bin/python3

#connect to this ip and port
import socket

HOST = "127.0.0.1"
PORT = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET = IPV4, SOCK_STREAM = port
s.connect((HOST,PORT))
