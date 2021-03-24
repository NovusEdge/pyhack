import socket
from IPy import IP
import nslooker


# TODO: complete the docs for this...

class Scanner():

    '''  '''

    def __init__(self):
        self.sock = socket.socket()
        self.sock.settimeout(0.5)


    def scan_port(self, port: int, ip_address: str):

        '''  '''

        try:
            self.sock.connect((ip_address, port))
            return f"[+] Port {port} is Open."
        except Exception:
            return f"[-] Port {port} is Closed."



    def is_used(self, port):

        '''  '''

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0




    def get_ip_address(self, domain, soa_out=False):

        '''  '''

        ips, soa =  nslooker.get_ipaddr(domain)
        return (ips.answer, soa.answer) if soa_out else (ips.answer, None)

    def dns_query(self, domain):

        '''  '''

        return nslooker.get_ipaddr(domain)
