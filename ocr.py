# coding: utf-8
import tr
import sys, cv2, time, os
from PIL import Image, ImageDraw, ImageFont
import numpy as np

_BASEDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(_BASEDIR)


def ocr_onepage(img_path):

    img_pil = Image.open(img_path)
    try:
        if hasattr(img_pil, '_getexif'):
            # from PIL import ExifTags
            # for orientation in ExifTags.TAGS.keys():
            #     if ExifTags.TAGS[orientation] == 'Orientation':
            #         break
            orientation = 274
            exif = dict(img_pil._getexif().items())
            if exif[orientation] == 3:
                img_pil = img_pil.rotate(180, expand=True)
            elif exif[orientation] == 6:
                img_pil = img_pil.rotate(270, expand=True)
            elif exif[orientation] == 8:
                img_pil = img_pil.rotate(90, expand=True)
    except:
        pass

    MAX_SIZE = 1600
    if img_pil.height > MAX_SIZE or img_pil.width > MAX_SIZE:
        scale = max(img_pil.height / MAX_SIZE, img_pil.width / MAX_SIZE)

        new_width = int(img_pil.width / scale + 0.5)
        new_height = int(img_pil.height / scale + 0.5)
        img_pil = img_pil.resize((new_width, new_height), Image.ANTIALIAS)

    color_pil = img_pil.convert("RGB")
    gray_pil = img_pil.convert("L")

    t = time.time()
    n = 1
    for _ in range(n):
        tr.detect(gray_pil, flag=tr.FLAG_RECT)
    print("time", (time.time() - t) / n)

    results = tr.run(gray_pil, flag=tr.FLAG_ROTATED_RECT)

    with open('/data/'+sys.argv[2],'a') as f:
        f.write('\n'+sys.argv[1]+'\n')
        for i, rect in enumerate(results):
            if len(rect[1])>0:
                print(rect[1], len(rect[1]))
                f.write(rect[1])
                if len(sys.argv)==3:
                    f.write("\n")
                    if len(rect[1]) < 20:
                        f.write("\n")
                elif len(rect[1]) < int(sys.argv[3]):
                    f.write("\n\n")
        f.close()

if __name__ == "__main__":
    ocr_onepage('/data/'+sys.argv[1])
