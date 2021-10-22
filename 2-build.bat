call 0-settings.bat

echo off
call lib.bat :color Building python client...
echo on

call lib.bat :print_color %PYTHON% --version

call lib.bat :ask