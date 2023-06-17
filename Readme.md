Docker https://github.com/myhub/tr

- Build docker image:

```
docker build . -t ajeep/tr-ocr:v2.3.1
```

- Run image and go into container:

```
docker run -it --rm --cpus=4 -v $(pwd):/data ajeep/tr-ocr:v2.3.1 /bin/sh
```

- Run image to OCR png/jpg to txt:

```
docker run -it --rm --cpus=4 -v $(pwd):/data -e uid=`id -u` ajeep/tr-ocr:v2.3.1
```

not link lines of one paragraph, see characters/line. 

```
docker run -it --rm --cpus=4 -v $(pwd):/data -e uid=`id -u` ajeep/tr-ocr:v2.3.1 24
```

link lines of one paragraph, only len(line)<24 will split paragraphs.

