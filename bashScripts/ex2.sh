#! /bin/bash

ls -l
read -p "please enter file name : " filename1 filename2
if [ "$filename1" ]; then
	if [ -z "$filename2" ]; then
		tac $filename1
	else
		cat $filename1
	fi
fi
