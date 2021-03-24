import socket
from IPy import IP
from nslooker import __get_ipaddr, __get_ports


# TODO: complete the docs for this...

class Scanner():

    '''  '''

    def __init__(self):
        self.sock = socket.socket()
        self.sock.settimeout(0.65)


    def connect(self, ip_address, port):

        '''  '''

        pass


    def scan_port(self, port, ip_address):

        '''  '''

        pass


    def get_ip_address(self, domain):

        '''  '''

        ips, soa =  __get_ipaddr(domain)
        return ips.answer, soa.answer

    def get_ports(self):
        return list(i for i in __get_ports())
