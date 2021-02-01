import glob
from functions.debug import debug
def storechar(input):
  debug(1, "Storing character '"+input+"'")
  glob.output+='+'*ord(input)
