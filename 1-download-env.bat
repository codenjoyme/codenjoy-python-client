call 0-settings.bat

@echo off
echo        [44;93m+-----------------------------------+[0m
echo        [44;93m!         Installing Python         ![0m
echo        [44;93m+-----------------------------------+[0m
echo on

if "%SKIP_PYTHON_INSTALL%"=="true" ( goto :skip )
if "%INSTALL_LOCALLY%"=="false" ( goto :skip )
if "%INSTALL_LOCALLY%"=="" ( goto :skip )

cd %ROOT%
IF EXIST %TOOLS%\python.zip (
    del %TOOLS%\python.zip
)
powershell -command "& { set-executionpolicy remotesigned -s currentuser; [System.Net.ServicePointManager]::SecurityProtocol = 3072 -bor 768 -bor 192 -bor 48; $client=New-Object System.Net.WebClient; $client.Headers['User-Agent']='PoweShell script';  $client.DownloadFile('%ARCH_PYTHON%','%TOOLS%\python.zip') }"
rd /S /Q %TOOLS%\..\.python
%ARCH% x -y -o%TOOLS%\..\.python %TOOLS%\python.zip
cd %ROOT%

call :ask

goto :eof

:skip
	echo off
	echo        [44;93m  Installation skipped:         [0m
	echo        [44;93m      INSTALL_LOCALLY=%INSTALL_LOCALLY%       [0m
	echo        [44;93m      SKIP_PYTHON_INSTALL=%SKIP_PYTHON_INSTALL%        [0m
	echo on
	goto :ask
goto :eof

:ask
    echo off
    echo        [44;93m+---------------------------------+[0m
    echo        [44;93m!    Press any key to continue    ![0m
    echo        [44;93m+---------------------------------+[0m
    echo on
    pause >nul
goto :eof