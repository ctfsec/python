#Author: Ibrahim Mutiu Olajide
#youtube: https://youtube.com/@ctf-sec

#importing modules
import socket
from colorama import Fore, Style

#Defining function
def portscannerv3():
    # Set the target IP and port
    target_ip = input("Enter Domain name or IP: ")
    start_port = int(input("Enter start port no: "))
    end_port = int(input("Enter end port no: "))

    #Iterating through specified port numbers
    for port in range(start_port, end_port+1):
        # Try to connect to the target IP and port
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s=s.connect((target_ip, port))
            service= socket.getservbyport(port)

            if s == 0:
                print(f"{Fore.RED}[{service}] port {port} is closed   on host {target_ip}{Style.RESET_ALL}")
            else:
                print(f"{Fore.GREEN}[{service}] port {port} is open   on host {target_ip}{Style.RESET_ALL}")
        except (socket.error,OSError):
            service=port
            print(f"{Fore.RED}[{service}] port {port} is closed   on host {target_ip}{Style.RESET_ALL}")
#Calling function
portscannerv3()
