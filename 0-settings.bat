echo off
call lib :color Setup variables...
echo on

if "%GAME_TO_RUN%"=="" ( set GAME_TO_RUN=mollymage)
if "%BOARD_URL%"==""   ( set BOARD_URL=https://dojorena.io/codenjoy-contest/board/player/dojorena5?code=953820862434373766)

set ROOT=%CD%

if "%SKIP_TESTS%"==""  ( set SKIP_TESTS=true)

set CODE_PAGE=65001
chcp %CODE_PAGE%

set TOOLS=%ROOT%\.tools
set ARCH=%TOOLS%\7z\7za.exe

rem Set to true if you want to ignore python installation on the system
if "%INSTALL_LOCALLY%"==""     ( set INSTALL_LOCALLY=true)

if "%INSTALL_LOCALLY%"=="true" ( set PYTHON_HOME=)

if "%PYTHON_HOME%"==""   ( set NO_PYTHON=true)
if "%NO_PYTHON%"=="true" ( set PYTHON_HOME=%ROOT%\.python)
if "%NO_PYTHON%"=="true" ( set PATH=%PYTHON_HOME%;%PATH%)

set PYTHON=%PYTHON_HOME%\python

echo off
call lib :color PATH=%PATH%
call lib :color PYTHON_HOME=%PYTHON_HOME%
echo on

set ARCH_URL=https://www.python.org/ftp/python/3.9.9/python-3.9.9-embed-amd64.zip
set ARCH_FOLDER=

set PYTHON_CLIENT_HOME=%ROOT%
