@echo off
if "%PYTHON_HOME%"=="" (
    call 0-settings.bat
)


echo [44;93m
echo        +-------------------------------------------------------------------------+
echo        !                Now we are starting python client...                     !
echo        +-------------------------------------------------------------------------+
echo [0m


SET PATH=%PYTHON_HOME%;%PATH%
call python main.py %GAME_TO_RUN% %BOARD_URL%

call :ask

goto :eof

:ask
    echo Press any key to continue
    pause >nul
goto :eof