# ------------------------------------------------------------------------------
import os, pathlib

PATH = pathlib.Path(__file__).parent.absolute()
os.chdir(PATH)

#NOTE: When this is run as a "-m  module" the contents here will be executed...
# ------------------------------------------------------------------------------

import sys
from src.port_scanner.scanner import Scanner

s = Scanner()
s.scan("google.com")
