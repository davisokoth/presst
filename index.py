import os
from libs import imgsearch
from libs import imagics
from reportlab.platypus import SimpleDocTemplate, Image

dirName = '/home/davisokoth/Downloads/mymages/'
presstFile = '/home/davisokoth/presst.pdf'

def findFast():
    return imgsearch.dl_images_fr_gs('revelation', dirName)

# findFast()

# directory = os.fsencode(dirName)
# pFilename = os.fsdecode(presstFile)

for filename in os.scandir(dirName):
    print('Adding: ' + filename.name)
    imagics.resizeImage(dirName + filename.name)
    doc = SimpleDocTemplate(presstFile, pagesize=(3000, 3000))
    parts = []
    parts.append(Image(filename))
    doc.build(parts)
    print('Done!!!!!!')
