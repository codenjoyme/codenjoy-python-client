call 0-settings.bat

echo off
call lib.bat :color Installing python...
echo on

if "%SKIP_PYTHON_INSTALL%"=="true" ( goto :skip )
if "%INSTALL_LOCALLY%"=="false" ( goto :skip )
if "%INSTALL_LOCALLY%"=="" ( goto :skip )

call lib.bat :install python %ARCH_URL% %ARCH_FOLDER%
call lib.bat :print_color %PYTHON% --version

call lib.bat :ask

goto :eof

:skip
	echo off
	call lib.bat :color Installation skipped
	call lib.bat :color INSTALL_LOCALLY=%INSTALL_LOCALLY%
	call lib.bat :color SKIP_PYTHON_INSTALL=%SKIP_PYTHON_INSTALL%
	echo on
	call lib.bat :ask
    goto :eof