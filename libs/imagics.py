import os
from PIL import Image

def resizeImage(infile):
    size = 3000, 3000
    try:
        outfile = infile
        im = Image.open(infile)
        im.resize(size)
        im.save(outfile, "JPEG")
    except IOError:
        print('Resize failed for %' % infile)