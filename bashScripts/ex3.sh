#! /bin/bash

arg1=$1
arg2=$2

if [ ${#arg1} -gt 3 ] && [ ${#arg2} -gt 3 ]; then
	echo All Good
else
	echo Not good
fi
