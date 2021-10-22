call 0-settings.bat

echo off
call lib :color Installing python...
echo on

if "%SKIP_PYTHON_INSTALL%"=="true" ( goto :skip )
if "%INSTALL_LOCALLY%"=="false" ( goto :skip )
if "%INSTALL_LOCALLY%"=="" ( goto :skip )

call lib :install python %ARCH_URL% %ARCH_FOLDER%
call lib :print_color %PYTHON% --version

call lib :ask

goto :eof

:skip
	echo off
	call lib :color Installation skipped
	call lib :color INSTALL_LOCALLY=%INSTALL_LOCALLY%
	call lib :color SKIP_PYTHON_INSTALL=%SKIP_PYTHON_INSTALL%
	echo on
	call lib :ask
    goto :eof