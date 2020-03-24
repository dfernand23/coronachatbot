#!/bin/bash

CSSEGIS_DIR="./cssegis"
CURRENT_DIR=$(pwd)

if [[ -d "$CSSEGIS_DIR" ]]
then
  echo "$CSSEGIS_DIR already exists, pull latest data"

  cd $CSSEGIS_DIR || return

  git pull

  cd "$CURRENT_DIR" || return
else
  echo "Create new folder"
  git clone https://github.com/CSSEGISandData/COVID-19.git $CSSEGIS_DIR
fi