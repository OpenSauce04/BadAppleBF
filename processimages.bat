@echo off
mkdir processedframes
FOR /L %%i IN (1,1,3288) DO (
  echo %%i/3288
  python asciify.py frames/frame%%i.png > processedframes/%%i.txt
)