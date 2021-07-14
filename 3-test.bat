@echo off
if "%GAME_TO_RUN%"=="" (
    call 0-settings.bat
)

SET PATH=%PYTHON_HOME%;%PATH%

@echo        +-------------------------------------------------------------------------+
@echo        !                       Now we are starting TESTS...                      !
@echo        +-------------------------------------------------------------------------+

set ROOT=%CD%

xcopy /y engine\*.py tests\engine\engine\
xcopy /y lib\*.py tests\engine\lib\
xcopy /y engine\*.py tests\games\%GAME_TO_RUN%\engine\
xcopy /y games\%GAME_TO_RUN%\*.py tests\games\%GAME_TO_RUN%\games\%GAME_TO_RUN%\
cd tests\engine
call python -m unittest discover
cd %ROOT%

cd tests\games\%GAME_TO_RUN%
call python -m unittest discover
cd %ROOT%

rd /S /Q tests\engine\engine
rd /S /Q tests\engine\lib
rd /S /Q tests\games\%GAME_TO_RUN%\engine
rd /S /Q tests\games\%GAME_TO_RUN%\games

call :ask

goto :eof

:ask
    echo Press any key to continue
    pause >nul
goto :eof
