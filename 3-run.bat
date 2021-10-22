call 0-settings.bat

echo off
call lib :color Starting python client...
echo on

call %PYTHON% main.py %GAME_TO_RUN% %BOARD_URL%

call lib :ask