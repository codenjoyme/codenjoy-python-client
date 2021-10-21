call 0-settings.bat

echo off
echo        [44;93m+----------------------------------------------+[0m
echo        [44;93m!       Now we are starting python client...   ![0m
echo        [44;93m+----------------------------------------------+[0m
echo on

call %PYTHON% main.py %GAME_TO_RUN% %BOARD_URL%

call :ask

goto :eof

:ask
    echo off
    echo        [44;93m+---------------------------------+[0m
    echo        [44;93m!    Press any key to continue    ![0m
    echo        [44;93m+---------------------------------+[0m
    echo on
    pause >nul
goto :eof