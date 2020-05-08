import paddlehub as hub
import matplotlib.pyplot as plt
import os
import matplotlib.image as mpimg 
import matplotlib
import random
from PIL import ImageFont,ImageDraw,Image

def transparent_back(img):
    img=img.convert('RGBA')
    sp=img.size
    width=sp[0]
    height=sp[1]
    for yh in range(height):
        for xw in range(width):
            dot=(xw,yh)
            color_d=img.getpixel(dot)
            if(color_d[3]==0):
                color_d=(255,255,255,255)
                img.putpixel(dot,color_d)
    plt.imshow(img)
    plt.show()
    return img

def fuse_back(img, background):
    a = random.randint(0,20)
    img = img.convert('RGBA')
    background = background.convert('RGBA')
    sp = img.size
    width = sp[0]
    height = sp[1]
    sp2 = background.size
    w = sp2[0]
    h = sp2[1]
    box = (a, a, a+w, a+h)
    background = background.crop(box)
    for yh in range(height):
        for xw in range(width):
            dot=(xw,yh)
            color_img = img.getpixel(dot)
            color_background = background.getpixel(dot)
            if(color_img[3]==0):
                img.putpixel(dot,color_background)
    return img
    
   def text_generate():
    phrase1 = ['Fashionable guy', 'Celebrity', 'Star', 'King', 'Contender', 'Lighter', 'Entrepreneur', 'Economist', 'Hero', 'Gambling monster']
    phrase2 = ['Asia', 'Ahowbiz', 'World', 'Pecado', 'Business community', 'Zuan', 'Wangzhe Canyon', 'Africa', 'Arctic', 'School']
    phrase3 = ['How to be the ', 'Person of the year:', 'People who change the world:']
    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,2)
    str1 = phrase3[c] 
    str2 = phrase1[a] +' of '+ phrase2[b]
    return str1, str2

#在这里修改照片路径，一键生成只需要修改这里的路径哦，上传图片地址就可以一键封面了呢！
input_path = 'inherent/inherent26.jpg'
#生成人像抠图
#DeepLabv3+ 是Google DeepLab语义分割系列网络的最新作，其前作有 DeepLabv1, DeepLabv2, DeepLabv3。在最新作中，作者通过encoder-decoder进行多尺度信息的融合，同时保留了原来的空洞卷积和ASSP层， 
#其骨干网络使用了Xception模型，提高了语义分割的健壮性和运行速率，在 PASCAL VOC 2012 dataset取得新的state-of-art performance。
#该PaddleHub Module使用百度自建数据集进行训练，可用于人像分割，支持任意大小的图片输入。
humanseg = hub.Module(name="deeplabv3p_xception65_humanseg")
img_path = [input_path]
result = humanseg.segmentation(data={"image":img_path})
seg_path = result[0]['processed']

img = Image.open(seg_path)
#可以尝试其它背景
background = Image.open('style2.jpg')
#融入背景
img2 = fuse_back(img, background)
#加入边框
img1 = Image.open(r'frame.jpg')
img2 = img2.resize((408, 439),Image.ANTIALIAS)
img1.paste(img2, (78, 210, 486, 649))
plt.imshow(img2)
plt.show()
plt.imshow(img1)
plt.show()
img1.save('final.png')
Font = ImageFont.truetype("simhei.ttf",26)
drawobj = ImageDraw.Draw(img1)
text1, text2 = text_generate()
#位置 文本 颜色
drawobj.text([92,550], text1, 'black', font=Font)
drawobj.text([92,580], text2, 'black', font=Font)
plt.imshow(img1)
plt.show()
img1.save('final1.png')
