#!/bin/bash

##########################
# author: leo
# environment setting   
# last change: 21 Oct 2019
##########################

echo "Checking Environment..."
if [ ! -x dici ]
then
    if [ ! -d /usr/bin ];
    then 
        # no /usr/bin
        echo "SUGGESTION: Manual installation will be better!"
        exit
    fi

    echo "env looks great."
    sudo cp ./dic /usr/bin
    sudo chmod +x /usr/bin/dic
    echo "enjoy!"
    cd `dirname $0`
    echo "python "`pwd`"/main.py"' "$string"' >> ./dic
else
    echo "ERROR: command conflict!@setup"
fi
    







