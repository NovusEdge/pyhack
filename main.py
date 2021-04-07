import subprocess
import argparse
import pathlib
import shutil
import sys
import os

#NOTE: When this is run as a "-m  module" the contents here will be executed...
#####################################################
ORIGIN  = os.getcwd()                               #
PATH    = pathlib.Path(__file__).parent.absolute()  #
os.chdir(PATH)                                      #
#####################################################

# processes ...

os.chdir(ORIGIN)
