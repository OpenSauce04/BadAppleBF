@echo off
mkdir processedframes
FOR /L %%i IN (1,1,6575) DO (
  echo %%i/6575
  python asciify.py frames/frame%%i.png > processedframes/%%i.txt
)