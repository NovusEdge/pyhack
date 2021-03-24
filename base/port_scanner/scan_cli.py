import scanner, io, codecs
import os, sys, pathlib, subprocess

origin = os.getcwd()
PATH = pathlib.Path(__file__).parent.absolute()
os.chdir(PATH)

s = scanner.Scanner()
target = input("[+] Enter the target domain: ")
print("[*] Scanning for ports...")
ip_addrs = s.get_ip_address(target)
ports = []

for i in ip_addrs:
    if i is not None:
        process = subprocess.run(['../../boost/bin/booster', '-ports=true', f'-ip={i[0]}'], timeout=0.6, capture_output=True)
        out = list(map(
            lambda x: x.strip(),
            codecs.decode(process.stdout, 'UTF-8').split("\n")
        ))
        ports += out

if ports != ['']:
    print("[*] Active Ports: ")
    for port in ports:
        print(f"[+] Port {port} is Open")
else:
    print("[-] No ports Open :(")

os.chdir(origin)
