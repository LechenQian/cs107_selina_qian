#!/usr/bin/env bash
# Coder:Michael Li; Sharer: Selina Qian



for f in $(find . -maxdepth 1 -type f);
do
	perms=$(stat -c '%a' $f)
	permsu=$(( ${perms: 0: 1}%2 ))
    	if [ $permsu == 1 ];
	then
    		echo "${f##*/}"


	fi

done
