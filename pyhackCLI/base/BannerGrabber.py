import datetime
import logging
import pathlib
import socket
import json
import time
import sys
import os
import re

from IPy import IP
from queue import Queue
from threading import Thread

class BannerGrabber():

    def __init__(self, errlogfile="log/error_log_{datetime.date.today()}.log"):
        try:
            f = open(errlogfile, "w")
            f.write('')
        except FileNotFoundError:
            print(f"[-] Couldn't find the log file: {errlogfile}\nRedirecting logging to default file")

            PATH = pathlib.Path(__file__).parent.absolute()
            os.chdir(PATH)

            f = open(errlogfile, "w")
            f.write('')

        finally:
            f.close()

        self.errlogfile = errlogfile


    def _check_ip(self, ip):
        try:
            IP(ip)
            return ip

        except ValueError:
            try:
                return socket.gethostbyname(ip)

            except:
                logger = logging.getLogger()
                logging.basicConfig(
                    filename=self.errlogfile,
                    filemode='a',
                    format='%(name)s - %(levelname)s - %(message)s'
                    )

                now_time = time.strftime("%H:%M:%S")
                logger.error(f"{now_time} E: Can't resolve target: {ip}")


    def grab_one(self, target: str, port: int, timeout=0.5):
        target = self._check_ip(target)
        logger = logging.getLogger()
        logging.basicConfig(
            filename=self.errlogfile,
            filemode='a',
            format='%(name)s - %(levelname)s - %(message)s'
            )

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((target, port))

            if result != 0:
                with open("helper_files/sock_err.json", "r") as f:
                    errs = json.load(f)

                now_time = time.strftime("%H:%M:%S")
                logger.error(f"{now_time} E:{result}:  {errs[str(result)]}")
                return

            try:
                banner = sock.recv(4096)
                return banner
            except Exception as e:
                now_time = time.strftime("%H:%M:%S")
                logger.error(f"{now_time} E: {e}")


    def _push_to_log(self, ip: str, port: int, q: Queue, timeout=0.5):
        res = self.grab_one(ip, port, timeout=timeout)

        if res:
            try:
                with open("helper_files/grab_buffer.txt", "w") as f:
                    f.write(f"[+] Banner(PORT: {port}):\n{res}\n\n")
            except IOError as ioerr:
                now_time = time.strftime("%H:%M:%S")
                logging.error(f"{now_time} E: {ioerr}")
        q.task_done()



    def grab(self, target: str, start_port:int, end_port:int, timeout=0.5):
        q = Queue(maxsize=65535)

        if start_port not in range(1, 65536) or end_port not in range(1, 65536):
            now_time = time.strftime("%H:%M:%S")
            logging.error(f"{now_time} E: Port Range Invalid: {start_port} to {end_port}")
            return

        for j in range(start_port, end_port):
            worker = Thread(target=self._push_to_log, args=(target, j, q, timeout))
            worker.setDaemon(True)
            worker.start()
            q.put(j)

        q.join()
