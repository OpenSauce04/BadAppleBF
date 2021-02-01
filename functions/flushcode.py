import glob
from functions.debug import debug
def flushcode():
  debug(1, "Flushing code...")
  glob.f.write(glob.output)
  glob.output=""
