import init
import glob
from functions.printtext import printtext
from functions.printframe import printframe
from functions.storechar import storechar
from functions.writeraw import writeraw
from functions.flushcode import flushcode

try:
  open('BadApple.bf', 'w').close() #wipe code
except:
  # Previous file does not exist, continue
  True # Empty instruction to stop python from complaining
print("Compiling to './BadApple.bf'...")
printtext(chr(27)+"[?25l") # Hide cursor
printtext(chr(27)+"[2J") # Clear screen
#storechar(" ")
#writeraw(">")
#storechar("@") TODO: optimize image storage using these
#writeraw("<")
#flushcode()
for x in range(1,3288):
  print("Frame "+str(x)+"...", end="")
  printframe("processedframes/"+str(x)+".txt")
  flushcode()
  print("done")
printtext(chr(27)+"[f") # Reset cursor
printtext("Demo Written by OpenSauce\n")
printtext("Thanks for watching!\n")
printtext(chr(27)+"[?25h") # Show cursor
flushcode()
glob.f.close()

print("done.")