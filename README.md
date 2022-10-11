This code is derived from [LabelImg](https://github.com/heartexlabs/labelImg).

# LabelImageLab

Lean and flexible code and gui for supervised learning image labeling.

This code have been tested on: Ubuntu 22.04

## Installation

Clone this repo
````bash
git clone git@github.com:SLU-Aqua/LabelImageLab.git
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
venv/bin/python3 labelImageLab.py -d /home/erik/tmp/rings3 -c data/bsp_ring_classes.txt
````
For help and more options
````bash
venv/bin/python3 labelImageLab.py -h
````


## Build app
