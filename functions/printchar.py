from os import write
import sys
from functions.writeraw import writeraw
from functions.debug import debug
import glob
def printchar(input):
  try:
    if sys.argv[2] == "--char":
      debug(1, "Writing character '"+input+"'")
  except:
    ''
  while (ord(input) != glob.bitcounter):
    if (ord(input)>glob.bitcounter):
      writeraw("+")
      glob.bitcounter+=1
    else:
      writeraw("-")
      glob.bitcounter-=1
  writeraw(".")
