#!/usr/bin/env bash

. 0-settings.sh

color $COLOR1 "Starting python client..."
echo

eval_echo "$PYTHON main.py $GAME_TO_RUN $BOARD_URL"

ask
