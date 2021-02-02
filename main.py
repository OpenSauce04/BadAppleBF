import init
import glob
from functions.printtext import printtext
from functions.printfile import printfile
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
  printfile("processedframes/"+str(x)+".txt")
  flushcode()
printtext(chr(27)+"[f") # Reset cursor
printtext("Demo Written by OpenSauce")
printtext("Thanks for watching!")
printtext(chr(27)+"[?25h") # Show cursor
flushcode()
glob.f.close()

print("done.")