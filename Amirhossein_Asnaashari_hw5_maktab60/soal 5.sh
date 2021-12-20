cd $1;
echo "Number of files :"  find . -mindepth 1 -maxdepth 1 -type f | wc -l;
echo "Number of directories : " find . -mindepth 1 -maxdepth 1 -type d | wc -l;