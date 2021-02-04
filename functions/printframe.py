import glob
from functions.writeraw import writeraw
from functions.printchar import printchar
from functions.printtext import printtext
from functions.flushcode import flushcode
from functions.debug import debug
import os.path
def printframe(path):
  debug(3, "Writing prerendered image at '"+path+"'")
  if not os.path.exists(path):
    print("ERROR: file not found: "+path)
  f = open(path, "r")
  printtext(chr(27)+"[f")
  writeraw("[-]")
  for c in f.read():
    if c=='b':
      writeraw("<.>")
      writeraw("++++++[-]") #Idle
    elif c=='w':
      writeraw(">[.>]<[<]")
    else:
      glob.bitcounter=0;
      printchar(c)
      writeraw("[-]")
  f.close
  flushcode()
