@echo off

call run :init_colors

:check_run_mode
    if "%*"=="" (       
        call :run_executable 
    ) else (
        call :run_library %*
    )
    goto :eof

:run_executable
    rem run stuff.bat as executable script
    call run :color ‘%CL_INFO%‘ ‘This is not executable script. Please use 'run.bat' only.‘
    call run :ask   
    goto :eof

:run_library
    rem run stuff.bat as library
    call %*     
    goto :eof          

:settings
    if "%INSTALL_LOCALLY%"=="true" ( set PYTHON_HOME=)

    if "%PYTHON_HOME%"==""   ( set NO_PYTHON=true)
    if "%NO_PYTHON%"=="true" ( set PYTHON_HOME=%ROOT%\.python)
    if "%NO_PYTHON%"=="true" ( set PATH=%PYTHON_HOME%;%PATH%)

    set PYTHON=%PYTHON_HOME%\python

    echo Language environment variables
    call run :color ‘%CL_INFO%‘ ‘PATH=%PATH%‘
    call run :color ‘%CL_INFO%‘ ‘PYTHON_HOME=%PYTHON_HOME%‘

    set ARCH_URL=https://www.python.org/ftp/python/3.9.9/python-3.9.9-embed-amd64.zip
    set ARCH_FOLDER=
    goto :eof

:install
    call run :install python %ARCH_URL% %ARCH_FOLDER%
    goto :eof

:version
    call run :eval_echo_color ‘%PYTHON% --version‘
    goto :eof

:build
    rem do nothing
    goto :eof

:test    
    call %ROOT%\run :eval_echo ‘xcopy /S/I/y %ROOT%\engine\* %ROOT%\temp\engine\‘
    call %ROOT%\run :eval_echo ‘xcopy /S/I/y %ROOT%\lib\* %ROOT%\temp\lib\‘
    call %ROOT%\run :eval_echo ‘xcopy /S/I/y %ROOT%\games\* %ROOT%\temp\games\‘
    call %ROOT%\run :eval_echo ‘cd %ROOT%\temp\‘
    call %ROOT%\run :sep

    call %ROOT%\run :color ‘%CL_HEADER%‘ ‘Engine tests...‘
    call %ROOT%\run :eval_echo ‘xcopy /S/I/y %ROOT%\tests\engine\* %ROOT%\temp\‘
    call %ROOT%\run :eval_echo ‘%PYTHON% -m unittest discover -vvv‘
    call %ROOT%\run :eval_echo ‘del /S /Q test_*.py‘
    call %ROOT%\run :sep

    call %ROOT%\run :color ‘%CL_HEADER%‘ ‘Clifford tests...‘‘
    call %ROOT%\run :eval_echo ‘xcopy /S/I/y %ROOT%\tests\games\clifford\* %ROOT%\temp\‘
    call %ROOT%\run :eval_echo ‘call %PYTHON% -m unittest discover -vvv‘
    call %ROOT%\run :eval_echo ‘del /S /Q test_*.py‘
    call %ROOT%\run :sep

    call %ROOT%\run :color ‘%CL_HEADER%‘ ‘Mollymage tests...‘‘
    call %ROOT%\run :eval_echo ‘xcopy /S/I/y %ROOT%\tests\games\mollymage\* %ROOT%\temp\‘
    call %ROOT%\run :eval_echo ‘call %PYTHON% -m unittest discover -vvv‘
    call %ROOT%\run :eval_echo ‘del /S /Q test_*.py‘
    call %ROOT%\run :sep

    call %ROOT%\run :color ‘%CL_HEADER%‘ ‘Sample tests...‘
    call %ROOT%\run :eval_echo ‘xcopy /S/I/y %ROOT%\tests\games\sample\* %ROOT%\temp\‘
    call %ROOT%\run :eval_echo ‘call %PYTHON% -m unittest discover -vvv‘
    call %ROOT%\run :eval_echo ‘del /S /Q test_*.py‘

    call %ROOT%\run :eval_echo ‘cd %ROOT%\‘
    call %ROOT%\run :eval_echo ‘rd /S /Q %ROOT%\temp‘
    call %ROOT%\run :sep
    goto :eof

:run
    call run :eval_echo ‘%PYTHON% main.py %GAME_TO_RUN% %SERVER_URL%‘
    goto :eof