FROM python:3.9-slim-bullseye AS tr-ocr
COPY ocr.* /usr/bin/

RUN set -e; pwd \
  && apt-get update && apt-get install -y git libgomp1 libgl1-mesa-glx libglib2.0-0 libsm6 libxrender1 libxext6 \
  && pip install opencv-python pillow \
#  && export https_proxy=http://192.168.1.26:7890 \
  && pip install git+https://github.com/myhub/tr.git@master \
#  && cd /root; git clone --depth 1 https://github.com/myhub/tr.git; cd tr; python setup.py install \
  && rm -rf /var/lib/apt/lists/*; apt clean

ENTRYPOINT [ "/usr/bin/ocr.sh" ]
WORKDIR /data

