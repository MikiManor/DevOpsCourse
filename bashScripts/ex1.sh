#! /bin/bash

cd /tmp
ls 
echo "start >>>"
touch mytempfile
echo "after file creation >>>"
ls 
mkdir mytempdir
echo "after dir creation >>>"
ls 
mv mytempfile mytempdir/
echo "after move >>>"
ls 
echo "in dir >>>"
ls mytempdir
rm -rf mytempdir
echo after remove
ls
