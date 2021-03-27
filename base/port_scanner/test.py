import socket
from colorama import Fore, init
from IPy import IP

# colors for fancy printing:
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX


def is_port_open(host, port, timeout=0.2):

    '''  '''

    sock = socket.socket()# creates a new socket

    try:
        sock.connect( (host, port) ) # tries to connect to host using that port
        sock.settimeout(timeout)

    except:
        return False # if cannot connect, the port is closed.

    else:
        return True # if the connection was established, port is open.

if __name__ == '__main__':
    host = input("[*] Enter the host: ") # get the host from the user

    for port in range(1, 100): # iterate over ports, from 1 to 100
        if is_port_open(host, port):
            print(f"{GREEN}[+] {host}:{port} is open      {RESET}")

        else:
            print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")
