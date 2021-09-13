grep -E -c '[0-9]+' apollo13.txt > apollo_out.txt
grep --help | grep -E '(--count)'
find . -maxdepth 1 -type f -name "*.py"|wc -l
find . -type f! -perm /006 |wc -l
find . -maxdepth 1! -perm /006 |wc -l 
