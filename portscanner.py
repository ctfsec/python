#Author: Ibrahim Mutiu Olajide
#youtube: https://youtube.com/@ctf-sec


#Importing modules
import socket

#Setting targetIP and TargetPort
target_ip = input("Enter IP Example XXX.XXX.XX.XXX ")
target_port = int(input("Enter target port Example 80 "))

#Creating a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Catching and Exception or Handling Error
try:
    s.connect((target_ip, target_port))
    print(f" Port {target_port} is open")
except socket.error:
    print(f" Port {target_port} is closed")