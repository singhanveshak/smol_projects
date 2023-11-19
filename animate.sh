#!/bin/bash

#Author: Anveshak Singh @singhanveshak
#Date: 19/11/2023
#This script reads in an video-> breaks it into few frames-> converts each frame to ascii art-> animates the script
#ascii-greyscale: " .:-=+*#%@" (lighter to darker brightness)
#USAGE: $> ./animate.sh vid.mp4

#generate ascii frames
python animate.py $1
file=$1.txt

while read -r line; do
if [ "$line" == "101" ];then
    sleep 0.04
    clear
else
    echo "$line"
    fi
done <$file 