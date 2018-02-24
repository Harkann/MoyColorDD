#! /usr/bin/env python3
from urllib import request
import png
import sys
url = sys.argv[1]
def get(url):
    req = request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with request.urlopen(req) as r:
        return r.read()


def download(url, file=None):
    if not file:
        file = url.split('/')[-1]
    with open(file, 'wb') as f:
        f.write(get(url))

download(url, "plop.png")
r=png.Reader(filename="plop.png")
#print(r.read())
img = list(r.asRGBA()[2])
#print(img)

def moye(image):
    rtot, gtot, btot, pix = 0,0,0,0
    for line in image:
        r, g, b, transp = 0,0,0,False
        for i in range(1, len(line), 4):
            if line[i+2] != 0:
                rtot += line[i-1]
                gtot += line[i]
                btot += line[i+1]
                pix+=1
    return rtot/pix, gtot/pix, btot/pix

r, g, b = moye(img)
print("http://duckduckgo.com/?q=rgb({},{},{})".format(int(r), int(g), int(b)))
#print(moye(img))
        
