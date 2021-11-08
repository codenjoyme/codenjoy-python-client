call 0-settings.bat

echo off
call lib :color Starting python tests...
echo on

xcopy /S/I/y test\* temp\
xcopy /S/I/y engine\* temp\engine\
xcopy /S/I/y lib\* temp\lib\
xcopy /S/I/y games\* temp\games\

echo off
call lib :color Engine tests...
echo on

xcopy /S/I/y tests\engine\* temp\
cd temp\
call %PYTHON% -m unittest discover
cd %ROOT%
rd /S /Q temp/test_*.py

echo off
call lib :color Clifford tests...
echo on

xcopy /S/I/y tests\games\clifford\* temp\
cd temp\
call %PYTHON% -m unittest discover
cd %ROOT%
rd /S /Q temp/test_*.py

echo off
call lib :color Mollymage tests...
echo on

xcopy /S/I/y tests\games\mollymage\* temp\
cd temp\
call %PYTHON% -m unittest discover
cd %ROOT%
rd /S /Q temp/test_*.py

echo off
call lib :color Sample tests...
echo on

xcopy /S/I/y tests\games\sample\* temp\
cd temp\
call %PYTHON% -m unittest discover
cd %ROOT%
rd /S /Q temp/test_*.py

rd /S /Q temp

call lib :sep

call lib :ask