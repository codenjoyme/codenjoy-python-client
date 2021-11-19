#!/usr/bin/env bash

. 0-settings.sh

color $COLOR1 "Starting python tests..."
echo

eval_echo "cp -rf test/* temp/"
eval_echo "cp -rf engine/* temp/engine/"
eval_echo "cp -rf lib/* temp/lib/"
eval_echo "cp -rf games/* temp/games/"

color $COLOR4 "Engine tests..."

eval_echo "cp -rf tests/engine/* temp/"
eval_echo "cd temp"
eval_echo "$PYTHON -m unittest discover"
eval_echo "cd %ROOT%"
eval_echo "rm -f ./temp/test_*.py"

color $COLOR4 "Clifford tests..."

eval_echo "cp -rf tests/games/clifford/* temp/"
eval_echo "cd temp"
eval_echo "$PYTHON -m unittest discover"
eval_echo "cd %ROOT%"
eval_echo "rm -f ./temp/test_*.py"

color $COLOR4 "Mollymage tests..."

eval_echo "cp -rf tests/games/mollymage/* temp/"
eval_echo "cd temp"
eval_echo "$PYTHON -m unittest discover"
eval_echo "cd %ROOT%"
eval_echo "rm -f ./temp/test_*.py"

color $COLOR4 "Sample tests..."

eval_echo "cp -rf tests/games/sample/* temp/"
eval_echo "cd temp"
eval_echo "$PYTHON -m unittest discover"
eval_echo "cd %ROOT%"
eval_echo "rm -f ./temp/test_*.py"

eval_echo "rm -rf ./temp"

sep

ask