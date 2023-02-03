#!/bin/bash

#!/bin/bash

set -e 

rm -rf venv
python.exe -m venv venv
./venv/Scripts/python.exe -m pip install --upgrade pip 
./venv/Scripts/pip.exe install --no-cache-dir -r requirements.txt

#case "$OSTYPE" in
#  solaris*) echo "SOLARIS" ;;
#  darwin*)  echo "OSX" ;; 
#  linux*)   echo "LINUX" ;;
#  bsd*)     echo "BSD" ;;
#  msys*)    echo "WINDOWS" ;;
#  cygwin*)  echo "ALSO WINDOWS" ;;
#  *)        echo "unknown: $OSTYPE" ;;
#esac


#rm -rf venv/
#python3 -m venv venv
#venv/bin/pip3 install --upgrade pip
#venv/bin/pip3 install -r requirements.txt 


