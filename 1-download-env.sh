#!/usr/bin/env bash

. 0-settings.sh

color $COLOR1 "Installing python..."
echo

eval_echo "[[ \"$SKIP_PYTHON_INSTALL\" == \"true\" ]] && skip"
eval_echo "[[ \"$INSTALL_LOCALLY\" == \"false\" ]] && skip"
eval_echo "[[ \"$INSTALL_LOCALLY\" == \"\" ]] && skip"

ask_message $COLOR4 "There is a need to update the system and install make. Should we update (y/n)?"
if [[ "$ask_result" == "y" ]]; then
   eval_echo "sudo apt -y update"
   eval_echo "sudo apt -y install make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev"
else
   color $COLOR4 "Skipped"
fi

ask_message $COLOR4 "There is a need to make openssl. Should we make (y/n)?"
if [[ "$ask_result" == "y" ]]; then
    eval_echo "install 'openssl-sources' '$OPENSSL_ARCH_URL' '$OPENSSL_ARCH_FOLDER'"

    eval_echo "sudo rm -rf $ROOT/.openssl"
    eval_echo "cd $ROOT/.openssl-sources"
    eval_echo "./config --prefix=$OPENSSL_HOME --openssldir=$OPENSSL_HOME"
    eval_echo "sudo make"
    eval_echo "sudo make install_sw"

    eval_echo "sudo ln -s /etc/ssl/certs $OPENSSL_HOME/certs"
else
   color $COLOR4 "Skipped"
fi

eval_echo_color_output "$OPENSSL version -a"

ask_message $COLOR4 "There is a need to make python. Should we make (y/n)?"
if [[ "$ask_result" == "y" ]]; then
    eval_echo "install 'python-sources' '$ARCH_URL' '$ARCH_FOLDER'"

    eval_echo "sudo rm -rf $ROOT/.python"
    eval_echo "cd $ROOT/.python-sources"
    eval_echo "./configure --enable-shared --with-openssl=$OPENSSL_HOME --prefix=$PYTHON_HOME"
    eval_echo "sudo make"
    eval_echo "sudo make install"

    eval_echo "sudo ldconfig $PYTHON_HOME/lib"
else
   color $COLOR4 "Skipped"
fi

eval_echo_color_output "$PYTHON --version"

ask

skip() {
    color $COLOR3 "Installation skipped"
    color $COLOR3 "INSTALL_LOCALLY=$INSTALL_LOCALLY"
    color $COLOR3 "SKIP_PYTHON_INSTALL=$SKIP_PYTHON_INSTALL"
    ask
    exit
}