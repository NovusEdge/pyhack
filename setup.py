import os
import pathlib

PATH = pathlib.Path(__file__).parent.absolute()
os.chdir(PATH)

os.system('pip install -r requirements.txt')
