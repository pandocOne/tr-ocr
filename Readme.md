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

    - link lines of one paragraph, only len(line)<24 will split paragraphs:

    ```
    docker run -it --rm --cpus=4 -v $(pwd):/data -e uid=`id -u` ajeep/tr-ocr:v2.3.1 24
    ```

    - not link lines of one paragraph, see characters/line:

    ```
    docker run -it --rm --cpus=4 -v $(pwd):/data -e uid=`id -u` ajeep/tr-ocr:v2.3.1
    ```

- then link lines of one paragraph

    ```
    sed -i ':a;N;$!ba;s/\([^\n]\)\n\([^\n]\)/\1\2/g' file
    # sed -e ':a' -e 'N' -e '$!ba' -e 's/\([^\n]\)\n\([^\n]\)/\1\2/g' file
    ```

    or you can `vim file`，then `:%s/\([^\\n]\)\n\([^\\n]\)/\1\2/g`

