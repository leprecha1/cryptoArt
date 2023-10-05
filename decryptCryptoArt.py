
from PIL import Image
import random
import json
import sys

nameOutput = sys.argv[2]
 
#img = Image.new('RGB', (60, 30), color = 'red')
#img.save('pil_red.png')
colors = json.loads(open("colors.py","r").read())
text = open(sys.argv[1],"r").read()
images = []

print(len(text))
print(900*900)

basewidth=1200
width = 900
height = 900

cont = 0
img  = Image.new( "RGB", (width, height), "#000000")
for linha in range(0, width):
    for coluna in range(0, height):
        try:
            img.putpixel((linha, coluna), eval(colors[(text[cont]).lower()]))
            if cont==len(text):
                img.putpixel((linha, coluna), eval(colors['[+END+]']))
        except Exception as ex:
            print(ex)
            img.putpixel((linha, coluna), (0,0,0))
        cont += 1

#wpercent = (basewidth/float(img.size[0]))
#hsize = int((float(img.size[1])*float(wpercent)))
#img = img.resize((basewidth,hsize), Image.ANTIALIAS)

img.save(nameOutput)
               
