#!/bin/sh

#docker run -it --rm --cpus=8 -v $(pwd):/data -e uid=`id -u` ajeep/tr-ocr:v2.3.1 24
docker run -it --rm --cpus=8 -v $(pwd):/data -e uid=`id -u` ajeep/tr-ocr:v2.3.1
# sed -i ':a;N;$!ba;s/\([^\n]\)\n\([^\n]\)/\1\2/g' file
