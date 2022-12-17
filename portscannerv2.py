#Author: Ibrahim Mutiu Olajide
#youtube: https://youtube.com/@ctf-sec

#Importing modules
import socket
from colorama import Fore, Style

# Set the target IP and port
target_ip = input("Enter Domain name or IP: ")
start_port = int(input("Enter start port no: "))
end_port = int(input("Enter end port no: "))

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Iterating through specified port numbers
for port in range(start_port, end_port+1):
# Try to connect to the target IP and port
    try:
        s.connect((target_ip, port))
        print(f"{Fore.GREEN}Port {port} is open   on host {target_ip}{Style.RESET_ALL}")
        
    except socket.error:
        print(f"{Fore.RED}Port {port} is closed on host {target_ip}{Style.RESET_ALL} ")