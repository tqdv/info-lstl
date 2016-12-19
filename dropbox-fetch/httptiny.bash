#!/bin/bash

TIME=`perl httptiny.pl "http://bit.ly/MPSI3_16-17";`;

sort filelist/filelist_${TIME}.txt > sorted_${TIME}.txt
mv sorted_${TIME}.txt filelist/filelist_${TIME}.txt

if [ -s lasttime ]
then
    LAST=`cat lasttime`
    diff filelist/filelist_${LAST}.txt filelist/filelist_${TIME}.txt > diff/diff_${TIME}.txt
fi

echo $TIME > lasttime
