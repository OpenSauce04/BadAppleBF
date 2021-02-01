@echo off
mkdir processedframes
FOR /L %%i IN (1,1,3289) DO (
  echo %%i/3289
  python asciify.py frames/frame%%i.png > processedframes/%%i.txt
)