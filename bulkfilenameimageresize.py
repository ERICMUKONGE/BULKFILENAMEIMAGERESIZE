import os
from pickletools import optimize
from PIL import Image

image_dir = os.listdir('items')

for image in image_dir:
    im = image.open('items'+ image)
    width, height = im.same
    new_width = 788
    ratio = new_width/width
    new_height = int(height * ratio)
    height = ((new_width,new_height))
    im = open('items/' + image,optimize=True, int(open,close))