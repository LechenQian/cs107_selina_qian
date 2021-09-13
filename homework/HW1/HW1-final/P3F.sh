for f in $(find . -maxdepth 1 -type f);
do
        echo -n ${f##*/}&& echo -n ' ' &&  wc -l<$f;

done
