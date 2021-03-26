import scanner, io, codecs
import os, sys, pathlib, subprocess

'''  '''

origin = os.getcwd()
PATH = pathlib.Path(__file__).parent.absolute()
os.chdir(PATH)

s = scanner.Scanner()
targets = input("[+] Enter Target(s) to scan(split the targets with \',\'): ")
print(         "[*] Scanning for ports...")

if ',' in targets:
    for ip_add in targets.split(','):
        print(f"\nNow scanning: {ip_add}:")
        s.scan(ip_add.strip())
else:
    s.scan(targets)
