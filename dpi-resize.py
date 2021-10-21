#!/usr/bin/python
from PIL import Image
import os, sys

path = "images/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if not item.startswith('.'):
            if os.path.isfile(path+item):
                im = Image.open(path+item)
                f, e = os.path.splitext(path+item)
                im.save(f + ' resized.jpg', 'JPEG', quality=70, dpi=(72, 72))

resize()