import subprocess
import colorama
import argparse
import pathlib
import shutil
import sys
import os

from base.VulnScanner import VulnScanner

#####################################################
PATH = pathlib.Path(__file__).parent.absolute()     #
os.chdir(PATH)                                      #
#####################################################


TARGET  = input(f"{ colorama.Fore.GREEN }[+] Enter the target: " )
if not TARGET:
    print( f"{colorama.Fore.RED}[-] Invalid Target {colorama.Style.RESET_ALL}" )
    sys.exit(-1)

LOWER   = input("[+] Enter Starting Port(default: 1) : " )
UPPER   = input("[+] Enter Ending Port(default: 1024): " )
LOGFILE = input("[+] Enter path to a log file if you wish to store the error"
                "logs of the script(Leave empty for default src/port_scanner/log)"
                "\n> " )
t_out   = input("[+] Enter timeout for scanning(leave blank for default 0.5): ")

try:
    if UPPER:
        UPPER = int(UPPER)
    else:
        UPPER = 1024

    if LOWER:
        LOWER = int(LOWER)
    else:
        LOWER = 1

except ValueError:
    print(f"{colorama.Fore.RED}[-] Invalid port range.{colorama.Fore.RESET}")
    sys.exit(-1)



try:
    if t_out: t_out = float(t_out)
    else: t_out = 0.5
except ValueError:
    print(f"{colorama.Fore.RED}[-] Invalid timeout value.{colorama.Fore.RESET}")
    sys.exit(-1)



if LOGFILE:
    s = PortScanner(errlogfile=LOGFILE)
else:
    s = PortScanner(errlogfile=f"base/log/error_log_{datetime.date.today()}.log")
