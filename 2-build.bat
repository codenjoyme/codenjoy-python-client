call 0-settings.bat

echo off
call lib :color Building python client...
echo on

call lib :print_color %PYTHON% --version

call lib :ask