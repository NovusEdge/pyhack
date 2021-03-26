import socket
from IPy import IP
import nslooker


# TODO: complete the docs for this...

class Scanner():

    '''  '''

    def __init__(self):
        pass


    def scan(self, target, port_range=range(81)):
        conv_ip = self.check_ip(target)

        print(f'''---------------Scanning Target: {target}---------------''')

        for i in port_range:
            _is_open, banner = self.is_port_open(i, conv_ip)

            if _is_open:
                if banner is None:
                    print(f"[+] Port {i} is Open")
                else:
                    print(f"[+] Port {i} is Open : {banner}")

        print(f'''-------------------------------------------------------''')


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


    def get_banner(self, size=1024):
        return sockObj.recv(size)

    def dns_query(self, domain):

        '''  '''

        return nslooker.dns_query(domain)

    def is_port_open(self, port, ip_address, give_banner=True):
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((ip_address, port))
            try:
                banner = self.get_banner(sock)
                
                if give_banner: return True, banner
                else: return True

            except Exception:
                if give_banner: return True, None
                else: return True

        except Exception:
            if give_banner: return False, None
            else: return False
