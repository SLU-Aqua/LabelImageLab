#!/bin/bash

rm -rf venv/
python3 -m venv venv
venv/bin/pip3 install --upgrade pip
#pip3 install --upgrade PyInstaller pyinstaller-hooks-contrib
venv/bin/pip3 install -r requirements.txt 


