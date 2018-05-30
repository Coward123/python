#!/usr/bin/env python
#-*-coding=utf-8-*-
import os
import shutil
import httplib2
from PIL import Image, ImageDraw, ImageFont, ImageColor
import sys
dir = sys.path[0] + "/QQHeadPhotos2/"
try:
    os.makedirs(dir)
except:
    shutil.rmtree(dir)
    os.makedirs(dir)

f = open(sys.path[0] + "/qqlist.txt", 'r')
qqlist = f.readlines()
f.close()
def add_num(img, num, filename):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype(sys.path[0]+"/arial.ttf", size=40)
    fillcolor = ImageColor.colormap.get('red')
    width, height = img.size
    draw.text((width-30, 0), str(num), font=myfont, fill=fillcolor )
    img.save(filename, 'jpeg')
    return 0
h=httplib2.Http()
num = 0
for target in qqlist:
    url = 'http://qlogo.store.qq.com/qzone/qqnumber/qqnumber/100'
    target = target[:-1]
    if len(target) == 0:
        continue
    print('当前QQ：' + target)
    url = url.replace('qqnumber', target)
    resp, content = h.request(url)
    filename = dir + target + "headPhoto" + '.jpg'
    open(filename, "wb").write(content)
    num += 1
    img = Image.open(filename)
    add_num(img, num, filename)
print('下载完成')
