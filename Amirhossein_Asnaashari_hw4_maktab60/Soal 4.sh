cd $1;
touch text.txt;
find . -mindepth 1 -maxdepth 1 -type f -exec cat >> text.txt {} \;
sed -n -e '5,10p' text.txt
