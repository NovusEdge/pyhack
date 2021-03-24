import socket
from IPy import IP
import nslooker


# TODO: complete the docs for this...

class Scanner():

    '''  '''

    def __init__(self):
        self.sock = socket.socket()
        self.sock.settimeout(0.65)


    def connect(self, ip_address, port):

        '''  '''

        try:
            self.sock.connect(ip_address, port)
            return 0, None

        except Exception as e:
            return 1, e


    def scan_port(self, port, ip_address):

        '''  '''

        exit, _ = self.connect(ip_address, port)

        if exit == 0:
            return f"[+] Port {port} is Open", exit

        elif exit == 1:
            return f"[+] Port {port} is Closed", exit


    def get_ip_address(self, domain):

        '''  '''

        ips, soa =  nslooker.get_ipaddr(domain)
        return ips.answer, soa.answer

    def get_ports(self):
        return list(i for i in nslooker.get_ports())


if __name__ == '__main__':
    s = Scanner()
    
