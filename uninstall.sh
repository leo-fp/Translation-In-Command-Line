#!/bin/bash
############################################
# author: leo
# remove system command dic and source codes
# last change: 24 Oct 2019
############################################

if [ -x dic ]
then
    # 删除系统命令dic
    sudo rm /usr/bin/dic
fi

# 删除源码
cd `dirname $0`
dir=`pwd`
sudo rm -r $dir
