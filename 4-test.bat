call 0-settings.bat

echo off
echo        [44;93m+------------------------------------------------+[0m
echo        [44;93m!       Now we are starting python tests...      ![0m
echo        [44;93m+------------------------------------------------+[0m
echo on

xcopy /S/I/y test\* temp\
xcopy /S/I/y engine\* temp\engine\
xcopy /S/I/y lib\* temp\lib\
xcopy /S/I/y games\* temp\games\

call :sep

xcopy /S/I/y tests\engine\* temp\
cd temp\
call %PYTHON% -m unittest discover
cd %ROOT%
rd /S /Q temp/test_*.py

call :sep

xcopy /S/I/y tests\games\clifford\* temp\
cd temp\
call %PYTHON% -m unittest discover
cd %ROOT%
rd /S /Q temp/test_*.py

call :sep

xcopy /S/I/y tests\games\mollymage\* temp\
cd temp\
call %PYTHON% -m unittest discover
cd %ROOT%
rd /S /Q temp/test_*.py

rd /S /Q temp

call :sep

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

:sep
    echo off
    echo [44;93m---------------------------------------------------------------------------------------[0m
    echo on
goto :eof
