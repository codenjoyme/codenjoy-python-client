if "%JAVA_CLIENT_HOME%"=="" (
    call 0-settings.bat
)

@echo off
echo [44;93m
echo        +-------------------------------------+
echo        !          Installing PYTHON          !
echo        +-------------------------------------+
echo [0m
echo on

cd %ROOT%
rd /S /Q %PYTHON_HOME%
IF EXIST %TOOLS%\python.zip (
    @echo Delete previouse downloaded file.
    del %TOOLS%\python.zip
)
@echo Downloading Python.zip
powershell -command "& { set-executionpolicy remotesigned -s currentuser; [System.Net.ServicePointManager]::SecurityProtocol = 3072 -bor 768 -bor 192 -bor 48; $client=New-Object System.Net.WebClient; $client.Headers['User-Agent']='PoweShell script';  $client.DownloadFile('%ARCH_PYTHON%','%TOOLS%\python.zip') }"
%ARCH% x -y %TOOLS%\python.zip -o%PYTHON_HOME%

cd %ROOT%

goto :eof

:ask
    echo Press any key to continue
    pause >nul
goto :eof
