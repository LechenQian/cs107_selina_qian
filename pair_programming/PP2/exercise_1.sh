#!/usr/bin/env bash

read -r -p "file to commit: "  file
git add $file
git status
read -r -p "Continue to commit?(Y or N) " answer
if [ "$answer" == "Y" ]
then
	read -r -p "Commit message: " message
	git commit -m "$message"
	git status
	read -r -p "Continue to push?(Y or N) " is_push
	if [ "$is_push" == "Y" ]
	then
		git push
	else
		exit 1
	fi
else
	exit 1
fi
