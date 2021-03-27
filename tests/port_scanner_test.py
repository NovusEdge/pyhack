import os, pathlib

from .base.port_scanner.scanner import Scanner

s = scanner.Scanner()
print(s.is_port_open("google.com", 80))
s.scan("github.com", start_port=70, end_port=1000)
