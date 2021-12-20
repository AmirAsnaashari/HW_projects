cd $1;
find . -mindepth 1 -maxdepth 1 -type f -name "*a*" -exec grep -Iq . {} \; -exec cp {} /home/mobiledev/Desktop/TEST_LAST \;