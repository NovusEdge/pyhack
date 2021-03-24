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

if __name__ == '__main__':
    s = Scanner()
    domain = "google.com"

    ip_addrs = s.get_ip_address(domain)
    print(ip_addrs)
    ip_address = ip_addrs[0][0]

    for i in range(75, 85):
        print(s.scan_port(i, ip_address))
