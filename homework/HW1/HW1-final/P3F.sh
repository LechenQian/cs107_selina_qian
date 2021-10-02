#!/usr/bin/env bash

for f in $(find . -maxdepth 1 -type f);
do
        echo "${f##*/} $(wc -l < $f)";

done
