if "%GAME_TO_RUN%"=="" ( set GAME_TO_RUN=mollymage)
if "%BOARD_URL%"==""  ( set BOARD_URL=http://127.0.0.1:8080/codenjoy-contest/board/player/0?code=000000000000)

set ROOT=%CD%

if "%PYTHON_CLIENT_HOME%"==""     ( set PYTHON_CLIENT_HOME=%ROOT%)
if "%PYTHON_HOME%"==""            ( set PYTHON_HOME=%PYTHON_CLIENT_HOME%\.python)
                  