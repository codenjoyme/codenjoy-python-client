if "%PYTHON_CLIENT_HOME%"=="" (
    call 0-settings.bat
)

echo off
echo [44;93m
echo        +-------------------------------------------------------------------------+
echo        !                   Now we are building php client...                     !
echo        +-------------------------------------------------------------------------+
echo [0m

SET PATH=%PYTHON_HOME%;%PATH%
call python --version


@call :ask

goto :eof

:ask
    @echo off
    echo Press any key to continue
    pause >nul
goto :eof