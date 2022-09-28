This code is derived from LabelImg.

# LabelImageLab

Lean and flexible code and gui for supervised learning image labeling.

This code have been tested on: Ubuntu 22.04

## Installation

Clone this repo
````bash
git clone git@github.com:BalticSeabird/DataLabelAndEdit.git
cd LabelImageLab
````

Setup virtual environment
````bash
sh setupvenv.sh
````

Build QT resources
````bash
venv/bin/pyrcc5 -o libs/resources.py resources.qrc
````

## Usage
For example 
````bash
venv/bin/python3 labelImg.py /home/erik/tmp/data/ data/bsp_ring_classes.txt
````

## Build app
