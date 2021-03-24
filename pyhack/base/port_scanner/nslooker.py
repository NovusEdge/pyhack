from nslookup import Nslookup
from contextlib import closing
import socket, subprocess
import os, sys

def get_ipaddr(domain):
    dns_query = Nslookup(dns_servers=["1.1.1.1"])
    ips_record = dns_query.dns_lookup(domain)
    soa_record = dns_query.soa_lookup(domain)

    return ips_record, soa_record

def get_ports():
    for port in range(1, 8081):
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            res = sock.connect_ex(('localhost', port))
            if res == 0:
                yield port
