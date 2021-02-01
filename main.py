import init
import glob
from functions.printtext import printtext
from functions.preimage import preimage
from functions.writeraw import writeraw
from functions.flushcode import flushcode

try:
  open('BadApple.bf', 'w').close() #wipe code
except:
  # Previous file does not exist, continue
  True # Empty instruction to stop python from complaining
print("Compiling to './BadApple.bf'...")

printtext(chr(27)+"[2J") # Clear screen
flushcode()
glob.f.close()

print("done.")