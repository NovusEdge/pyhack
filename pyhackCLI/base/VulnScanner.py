import datetime
import logging
import pathlib
import socket
import shutil
import json
import time
import sys
import os

from IPy import IP
from queue import Queue
from threading import Thread

#####################################################
PATH = pathlib.Path(__file__).parent.absolute()     #
os.chdir(PATH)                                      #
#####################################################

from PortScanner import PortScanner

class VulnScanner():
    def __init__(self, errlogfile=f"log/error_log_{datetime.date.today()}.log"):
        self.port_scanner = PortScanner(errlogfile=errlogfile)


    def scan(self, ip: str, start_port=1, end_port=1024, timeout=0.5):
        q = Queue(maxsize=65535)

        if start_port not in range(1, 65536) or end_port not in range(1, 65536):
            now_time = time.strftime("%H:%M:%S")
            logging.error(f"{now_time} E: Port Range Invalid: {start_port} to {end_port}")
            return

        for j in range(start_port, end_port):
            worker = Thread(target=self._push_to_log, args=(ip, j, q, timeout))
            worker.setDaemon(True)
            worker.start()
            q.put(j)

        q.join()

if __name__ == '__main__':
    v = VulnScanner()
