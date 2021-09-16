
#!/usr/bin/env bash
# Coder:Michael Li; Sharer: Selina Qian



for f in $(find . -maxdepth 1 -type f);
do
	perms=$(stat -c '%a' $f)
	if [ $((0$perms & 0100)) -ne 0 ];
	then
    		echo "${f##*/}"
		

	fi

done
