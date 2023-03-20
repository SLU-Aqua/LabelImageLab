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
For example in Linux
````bash
venv/bin/python labelImageLab.py -c path_to_your_classes_file.txt
````
or in Windows
````bash
venv/Scripts/python labelImageLab.py -c path_to_your_classes_file.txt
````

For help and more options
````bash
venv/bin/python labelImageLab.py -h
````


## Build app
