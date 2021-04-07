import socket, logging
import sys, os, shutil, pathlib
import json, datetime, time
from IPy import IP
from queue import Queue
from threading import Thread

PATH = pathlib.Path(__file__).parent.absolute()
os.chdir(PATH)

class Scanner():
    def __init__(self, errlogfile=f"log/error_log_{datetime.date.today()}.log"):
        try:
            f = open(errlogfile)
        except IOError:
            f = open(errlogfile, "w")
            f.write('')
        finally:
            f.close()

        self.errlogfile = errlogfile

    def clear_logs():
        shutil.rmtree('log')
        os.mkdir('log')

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



    def is_port_open(self, ip: str, port: int, timeout=0.5):
        ip = self._check_ip(ip)
        logger = logging.getLogger()
        logging.basicConfig(
            filename=self.errlogfile,
            filemode='a',
            format='%(name)s - %(levelname)s - %(message)s'
            )


        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))

            if result != 0:
                with open("sock_err.json", "r") as f:
                    errs = json.load(f)


                now_time = time.strftime("%H:%M:%S")
                logger.error(f"{now_time} E:{result}:  {errs[str(result)]}")

                return False, -1
            else:
                return True, port

    def _push_to_log(self, ip: str, port: int, q: Queue):
        res, p = self.is_port_open(ip, port)

        if res:
            try:
                with open("log/ports_buffer.txt", "w") as f:
                    f.write(f"[+] Port {port} is Open.\n")
            except IOError as ioerr:
                now_time = time.strftime("%H:%M:%S")
                logging.error(f"{now_time} E: {ioerr}")
        q.task_done()


    def scan(self, ip: str, start_port=1, end_port=1024):
        q = Queue(maxsize=65535)

        if start_port not in range(1, 65536) or end_port not in range(1, 65536):
            now_time = time.strftime("%H:%M:%S")
            logging.error(f"{now_time} E: Port Range Invalid: {start_port} to {end_port}")
            return

        for j in range(start_port, end_port):
            worker = Thread(target=self._push_to_log, args=(ip, j, q))
            worker.setDaemon(True)
            worker.start()
            q.put(j)

        q.join()

if __name__ == '__main__':
    s = Scanner()
    s.scan("google.com", start_port=1, end_port=1024)
