if "%GAME_TO_RUN%"=="" ( set GAME_TO_RUN=mollymage)
if "%BOARD_URL%"==""   ( set BOARD_URL=http://127.0.0.1:8080/codenjoy-contest/board/player/0?code=000000000000)

set ROOT=%CD%

if "%SKIP_TESTS%"=="" ( set SKIP_TESTS=true)

set CODE_PAGE=65001
chcp %CODE_PAGE%

set TOOLS=%ROOT%\.tools
set ARCH=%TOOLS%\7z\7za.exe

rem Set to true if you want to ignore jdk and maven installed on the system
if "%INSTALL_LOCALLY%"=="" ( set INSTALL_LOCALLY=true)

if "%INSTALL_LOCALLY%"=="true" ( set PYTHON_HOME=)
if "%PYTHON_HOME%"=="" ( set NO_PYTHON=true)
if "%NO_PYTHON%"=="true" ( set PYTHON_HOME=%ROOT%\.python)
if "%NO_PYTHON%"=="true" ( set PATH=%PYTHON_HOME%;%PATH%)
set PYTHON=%PYTHON_HOME%\python

echo off
echo        [44;93mPYTHON_HOME=%PYTHON_HOME%[0m
echo on

set ARCH_PYTHON=https://www.python.org/ftp/python/3.9.6/python-3.9.6-embed-amd64.zip
set ARCH_PYTHON_FOLDER=

set PYTHON_CLIENT_HOME=%ROOT%
