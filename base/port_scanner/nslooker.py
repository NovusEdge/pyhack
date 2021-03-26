from nslookup import Nslookup
from contextlib import closing
import socket, subprocess
import os, sys

def dns_query(domain):
    dns_query = Nslookup(dns_servers=["1.1.1.1"])
    ips_record = dns_query.dns_lookup(domain)
    soa_record = dns_query.soa_lookup(domain)

    return ips_record, soa_record
