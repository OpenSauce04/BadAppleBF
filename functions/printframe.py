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
  for c in f.read():
    if c=='b':
      printchar(' ')
    elif c=='w':
      printtext("\xE2\x96\x88")
    else:
      printchar(c)
  f.close
  flushcode()
