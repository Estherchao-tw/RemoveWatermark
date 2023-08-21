from itertools import product
from PIL import Image

img = Image.open('watermark.jpg')
width,height = img.size
for pos in product(range(width),range(height)):
    if sum(img.getpixel(pos)[:3]) > 550:
        img.putpixel(pos,(255,255,255))
img.save("removewatermark1.png")