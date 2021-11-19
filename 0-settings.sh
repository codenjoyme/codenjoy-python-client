#!/usr/bin/env bash

. lib.sh

color $COLOR1 "Setup variables..."
echo

eval_echo "[[ \"$GAME_TO_RUN\" == \"\" ]] && GAME_TO_RUN=mollymage"
eval_echo "[[ \"$BOARD_URL\" == \"\" ]]   && BOARD_URL=http://127.0.0.1:8080/codenjoy-contest/board/player/0?code=000000000000"

eval_echo "ROOT=$PWD"

eval_echo "[[ \"$SKIP_TESTS\" == \"\" ]]  && SKIP_TESTS=true"

eval_echo "TOOLS=$ROOT/.tools"
eval_echo "ARCH=tar"

# Set to true if you want to ignore python installation on the system
eval_echo "[[ \"$INSTALL_LOCALLY\" == \"\" ]]   && INSTALL_LOCALLY=true"

eval_echo "[[ \"$INSTALL_LOCALLY\" == "true" ]] && export PYTHON_HOME="

eval_echo "[[ \"$PYTHON_HOME\" == \"\" ]]   && NO_PYTHON=true"
eval_echo "[[ \"$NO_PYTHON\" == \"true\" ]] && export PYTHON_HOME=$ROOT/.python"
eval_echo "[[ \"$NO_PYTHON\" == \"true\" ]] && export PATH=$PYTHON_HOME/bin:$PATH"

eval_echo "[[ \"$NO_PYTHON\" == \"true\" ]] && export OPENSSL_HOME=$ROOT/.openssl"
eval_echo "[[ \"$NO_PYTHON\" == \"true\" ]] && export PATH=$OPENSSL_HOME/bin:$PATH"
eval_echo "[[ \"$NO_PYTHON\" == \"true\" ]] && export LD_LIBRARY_PATH=$OPENSSL_HOME/lib:$LD_LIBRARY_PATH"

eval_echo "PYTHON=$PYTHON_HOME/bin/python3.7"
eval_echo "OPENSSL=$OPENSSL_HOME/bin/openssl"

color $COLOR4 "PATH=$PATH"
color $COLOR4 "PYTHON_HOME=$PYTHON_HOME"
echo

eval_echo "ARCH_URL=https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tgz"
eval_echo "ARCH_FOLDER=Python-3.7.7"

eval_echo "OPENSSL_ARCH_URL=https://www.openssl.org/source/openssl-1.1.1d.tar.gz"
eval_echo "OPENSSL_ARCH_FOLDER=openssl-1.1.1d"

eval_echo "PYTHON_CLIENT_HOME=$ROOT"