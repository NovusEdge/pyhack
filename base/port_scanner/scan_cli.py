import scanner, io, codecs
import os, sys, pathlib, subprocess

'''  '''

origin = os.getcwd()
PATH = pathlib.Path(__file__).parent.absolute()
os.chdir(PATH)

s = scanner.Scanner()
target = input("[+] Enter the target domain: ")
print(         "[*] Scanning for ports...")

target = s.check_ip(target)

for i in range(75, 85):
    print(s.scan_port(i, target))

os.chdir(origin)
