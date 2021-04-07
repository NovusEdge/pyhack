# ------------------------------------------------------------------------------
import os, pathlib

PATH = pathlib.Path(__file__).parent.absolute()
os.chdir(PATH)

#NOTE: When this is run as a "-m  module" the contents here will be executed...
# ------------------------------------------------------------------------------

import sys, subprocess
from src.port_scanner import port_scanner

s = port_scanner.Scanner()
