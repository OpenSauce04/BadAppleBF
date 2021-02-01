import sys
def debug(level,text):
  try:
    if sys.argv[1] == "--debug":
      print((' ' * level)+text)
  except:
    ''