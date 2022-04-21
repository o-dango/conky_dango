#!/bin/bash
track=$1
if (( $(expr length "$track") >= 30 ))
then
    echo "\${scroll 60 3 $track}"
else
    echo "$track"
fi
