#! /bin/bash

arg1=$1
arg2=$2

if [ ${#arg1} -gt 3 ] && [ ${#arg2} -gt 3 ]; then
	echo All Good
	if [ ${arg1} == ${arg2} ]; then
		echo both args are equal
	else
		echo args are different
	fi
else
	echo Not good
	exit 3
fi
