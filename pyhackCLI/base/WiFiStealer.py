import subprocess
import datetime
import logging
import pathlib
import smtplib
import socket
import shutil
import shlex
import json
import time
import sys
import os
import re

from queue import Queue
from threading import Thread

SUBPIPE = subprocess.PIPE

class WifiStealer(object):

    def __init__(self):
        pass

    def scan(self):
        pass
