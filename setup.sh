#!/bin/bash

##########################
# author: leo
# environment setting   
# last change: 21 Oct 2019
##########################

echo "Checking Environment..."
if [ ! -x dic ]
then
    if [ ! -d /usr/bin ];
    then 
        # no /usr/bin
        echo "SUGGESTION: Manual installation will be better!"
        exit
    fi

    echo "env looks great."
    cd `dirname $0`
    echo "python "`pwd`"/main.py"' "$string"' >> ./dic
    sudo cp ./dic /usr/bin
    sudo chmod +x /usr/bin/dic
    echo "enjoy!"
else
    echo "ERROR: command conflict!@setup"
fi
    







