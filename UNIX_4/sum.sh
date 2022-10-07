#!/usr/bin/bash -l
SUM=0
COUNT=10
if [ ! -z $1 ]; then
 echo "first cmdline arg is $1"
 COUNT=$1
fi
for n in $(seq $COUNT)
do
 echo "n is $n"
 SUM=$(expr $SUM + $n)
done
echo "SUM is $SUM"
