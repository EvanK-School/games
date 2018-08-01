#!/usr/bin/env bash

ARGS=($@)
games_dir=$(ls -l $(which game) | awk '{ print $NF; }')
games_dir=${games_dir%/*}
cd $games_dir && ./$1.* ${ARGS[*]:1}
