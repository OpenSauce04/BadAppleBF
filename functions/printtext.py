from functions.printchar import printchar
from functions.writeraw import writeraw
from functions.debug import debug
import glob
def printtext(input):
  debug(2, "Writing text '"+input+"'")
  writeraw("[-]")
  glob.bitcounter=0
  for x in range(0,len(input)):
    printchar(input[x])
