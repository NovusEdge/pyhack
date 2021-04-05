from .base import port_scanner

s = scanner.Scanner()
print(s.is_port_open("google.com", 80))
s.scan("github.com", start_port=1, end_port=500)
