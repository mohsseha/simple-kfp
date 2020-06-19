#!/bin/bash

CWD=`pwd`
for i in comp_*
do
    echo building $i 
    cd $i 
    ./build_comp.sh || exit 
    cd $CWD
done