#!/bin/bash
#echo $#
#index=1
string=""
for arg in $*
do 
    #echo "arg$index = $arg"
    string=$string$arg" "
    #echo "string = $string"
    let index+=1
done
#echo $string
python /home/pf/公共的/Translation-In-Command-Line/main.py "$string"
