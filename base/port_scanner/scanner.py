import socket
from IPy import IP
import nslooker


# TODO: complete the docs for this...

class Scanner():

    '''  '''

    def __init__(self):
        pass


    def scan_port(self, port: int, ip_address: str, timeout=0.5):

        '''  '''

        sock = socket.socket()
        sock.settimeout(timeout)

        try:
            sock.connect((ip_address, port))
            return f"[+] Port {port} is Open."
        except Exception:
            return f"[-] Port {port} is Closed."



    def is_used(self, port):

        '''  '''

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0




    def check_ip(self, ip_address: str):

        '''  '''

        try:
            IP(ip_address)
            return ip_address
        except ValueError:
            return socket.gethostbyname(ip_address)



    def dns_query(self, domain):

        '''  '''

        return nslooker.dns_query(domain)
