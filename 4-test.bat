call 0-settings.bat

echo off
call lib.bat :color Starting python tests...
echo on

xcopy /S/I/y test\* temp\
xcopy /S/I/y engine\* temp\engine\
xcopy /S/I/y lib\* temp\lib\
xcopy /S/I/y games\* temp\games\

call lib.bat :sep

xcopy /S/I/y tests\engine\* temp\
cd temp\
call %PYTHON% -m unittest discover
cd %ROOT%
rd /S /Q temp/test_*.py

call lib.bat :sep

xcopy /S/I/y tests\games\clifford\* temp\
cd temp\
call %PYTHON% -m unittest discover
cd %ROOT%
rd /S /Q temp/test_*.py

call lib.bat :sep

xcopy /S/I/y tests\games\mollymage\* temp\
cd temp\
call %PYTHON% -m unittest discover
cd %ROOT%
rd /S /Q temp/test_*.py

rd /S /Q temp

call lib.bat :sep

call lib.bat :ask