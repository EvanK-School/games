#!/usr/bin/env bash

open -a 'beaker browser' 'dat://exploder-creationix.hashbase.io/' 2>/dev/null

if [ "$?" == "1" ]; then
  echo
  echo 'Application "Beaker Browser" not found.'
  echo 'Please install "Beaker Browser" from'
  echo 'https://beakerbrowser.com/'
  echo
fi
