#!/bin/bash


### Ubuntu use pyinstall v3.0
#THIS_SCRIPT_PATH=`readlink -f $0`
#THIS_SCRIPT_DIR=`dirname ${THIS_SCRIPT_PATH}`
#cd bundle/linux
#git clone git@github.com:SLU-Aqua/LabelImageLab.git
#git checkout v3.2
#cd ${THIS_SCRIPT_DIR}

rm -r build
rm -r dist
rm labelImageLab.spec

venv/bin/pyinstaller --onefile \
            --hidden-import=xml \
            --hidden-import=xml.dom \
            --hidden-import=xml.etree \
            --hidden-import=xml.etree.ElementTree \
            --hidden-import=lxml.etree \
            --add-data "../../libs/*.py:libs" \
             ../../labelImageLab.py

# python pyinstaller/pyinstaller.py --hidden-import=xml \
#             --hidden-import=xml.etree \
#             --hidden-import=xml.etree.ElementTree \
#             --hidden-import=lxml.etree \
#              -D -F -n labelImg -c "../labelImg.py" -p ../libs -p ../

#FOLDER=$(git describe --abbrev=0 --tags)
#FOLDER="linux_"$FOLDER
#rm -rf "$FOLDER"
#mkdir "$FOLDER"
#cp dist/labelImg $FOLDER
#cp -rf ../data $FOLDER/data
#zip "$FOLDER.zip" -r $FOLDER
