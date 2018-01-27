#!/bin/bash
for x in $(ls); do 
	git add $x;
done;
c="update"
if [ "$1" != "" ]; then c=$1; fi
echo "Changed commit: $c"
git commit -m "$c"
git push origin master
