#!/bin/bash

# vim install
sudo apt-get --purge remove vim-common vim-tiny -y
sudo apt-get install vim -y

# fastapi
pip install fastapi uvicorn

# raspberrypi-server
