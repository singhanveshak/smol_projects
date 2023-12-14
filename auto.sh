#!/bin/bash
#This script will automate assembling and linking and GDBing for you
#please run this script with an argument as follows: $./auto.sh myprog
#if you want to makae your life easier please install gef plugin for gdb from: https://github.com/hugsy/gef

file=$1
nasm -f elf64 -o $file.o $file.s

status=$?
if [ -f $file.o ]; then
	#ld -m elf_i386 $file.o -o $file.out 
	ld $file.o -o a.out 
	status=$?
fi

if [ $status -eq 0 ]; then
	gdb a.out 
	clear
else
	echo  -e "------------------------------------\n\t\tPLEASE CORRECT ERROR\n------------------------------------"
fi

