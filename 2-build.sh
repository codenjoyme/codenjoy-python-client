#!/usr/bin/env bash

. 0-settings.sh

color $COLOR1 "Building python client..."
echo

eval_echo_color_output "$PYTHON --version"

ask
