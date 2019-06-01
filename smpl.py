from PIL import Image
im = Image.open('v.jpg','r')

size = width,height = im.size;

coordinate = x,y = 256,256
pl = im.getpixel( coordinate )
p2 = list(im.getdata())
print (pl)
print (p2)
