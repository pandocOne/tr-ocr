#!/bin/sh

set +e

files=`ls *.png *.jpg|sort`
fn=`date +%Y%m%d-%H%M%S`

for file in $files; do
  echo $file>>error.log
  python /usr/bin/ocr.py $file $fn.txt $1 2>>error.log
done
