import colorama
import logging
import pathlib
import sys
import os

from base.BannerGrabber import BannerGrabber

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
    b = BannerGrabber(errlogfile=LOGFILE)
else:
    b = BannerGrabber()

b.grab(TARGET, LOWER, UPPER, timeout=t_out)

os.chdir(PATH)

print(  "="*60 +
        f"\n{colorama.Fore.YELLOW}[*] Grabbing banners from target - {TARGET}."
        f"{colorama.Fore.RESET}\n")


try:
    with open("base/helper_files/grab_buffer.txt", 'r') as f:
        banners = f.read().split('\n')


    for banner in banners:
        print(f"{colorama.Fore.GREEN}{banner}")

    print(colorama.Style.RESET_ALL)

except IOError as i:
    logging.error(i)
