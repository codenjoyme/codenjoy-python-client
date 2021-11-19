#!/usr/bin/env bash

. 0-settings.sh

color $COLOR1 "Starting python tests..."
echo

eval_echo "rm -rf ./temp"

eval_echo "mkdir temp/"
eval_echo "cp -rf tests/* temp/"

eval_echo "cp -rf engine/* temp/engine/"

eval_echo "mkdir temp/lib/"
eval_echo "cp -rf lib/* temp/lib/"

eval_echo "cp -rf games/* temp/games/"

eval_echo "cd temp"
eval_echo "$PYTHON -m unittest discover -vvv"
eval_echo "cd %ROOT%"

eval_echo "rm -rf ./temp"

ask