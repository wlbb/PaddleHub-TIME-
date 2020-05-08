# PaddleHub 之 一键带你登上《TIME》时代周刊封面

想登上《TIME》时代周刊封面吗？快来试试吧！本项目基于PaddleHub中的等预训练模型，实现一键抠图，图片融合，随机文本生成等功能。快速上手，炒鸡简单！！！
本项目可以在百度大脑AIstudio中直接运行哦！传送门https://aistudio.baidu.com/aistudio/projectdetail/447445

---
## 内容

- [背景](#背景)
- [步骤思路](#步骤思路)
- [结果](#结果)
- [致谢](#致谢)

## 背景

### 任务简介

本项目基于百度飞桨paddlehub预训练模型训练工具，调用了图像分割库中的模型deeplabv3p_xception65_humanseg进行二次开发

本项目的目录结构如下：
```
├── time.py 主程序
│ 
├── test.jpg 测试图片
├── style.jpg 风格图片
├── frame.jpg 封面框架图片

```






## 步骤思路

1.首先将人像轮廓图片从照片中提取出来

2.然后将提取出来的人像图片和一张随机背景融合

3.将整张图片的风格进行迁移（可选，诙谐风格）

4.随机生成封面人物标签（爬取杂志封面中出现最频繁的词汇按照文法规则进行随机拼接，可以参考语言生成网络，由于本项目所需数据量小，于是自定义了一个函数）

5.最后将图片放缩至合适的格式粘贴到准备好的封面框中，并将标签写入图片。

### 相关函数介绍

#随机文本生成函数，定义了一些封面的热门词汇进行随机拼接（手动狗头）
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
  
#图像融合函数，将人像轮廓图片背景融合
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
    
#风格迁移，调用paddlehub中的stylepro_artistic模型，可以对图像的风格进行转换

stylepro_artistic = hub.Module(name="stylepro_artistic")

result = stylepro_artistic.style_transfer(
    
    images=[{
        'content': cv2.imread('test.png'),
        'styles': [cv2.imread('style.jpg')]
    }], 
    
    alpha=1.5,
    
    use_gpu=True,
    
    visualization=True,
    
    output_dir='transfer_result')
    
### 安装说明
**安装[PaddlePaddle](https://github.com/PaddlePaddle/Paddle)：**

在当前目录下运行样例代码需要PadddlePaddle Fluid的v.1.7.1或以上的版本。如果你的运行环境中的PaddlePaddle低于此版本，请根据[安装文档](https://www.paddlepaddle.org.cn/documentation/docs/zh/1.5/beginners_guide/install/index_cn.html)中的说明来更新PaddlePaddle。

其他依赖包：
安装paddlehub中人像抠图的预训练模型

!hub install deeplabv3p_xception65_humanseg

DeepLabv3+ 是Google DeepLab语义分割系列网络的最新作，其前作有 DeepLabv1, DeepLabv2, DeepLabv3。
在最新作中，作者通过encoder-decoder进行多尺度#信息的融合，同时保留了原来的空洞卷积和ASSP层， 
其骨干网络使用了Xception模型，提高了语义分割的健壮性和运行速率，在 PASCAL VOC 2012 dataset取得新的state-of-art performance。
该PaddleHub Module使用百度自建数据集进行训练，可用于人像分割，支持任意大小的图片输入。


### 数据准备
可以自行准备一张人像照片用于测试，或者使用项目包中提供的

## 结果

## 致谢

受七天打卡营的启发，于是做了这个项目参加paddlehub创意赛，paddlehub真的是个非常不错的预训练模型的应用工具，上手很简单，模型也很强大！

七天的训练营下来我感到非常充实，感谢百度飞桨团队这次举办的AI训练营，七天下来我收获颇多，对百度深度学习的框架有了更多深层次的了解，学习到了很多知识，受益匪浅！

在这里送给百度飞桨AI小鸭团队五星好评！！！炒鸡nice的课程，希望大家多多关注！！！

非常期待接下来的论文复现营和竞赛训练营！大家一起加油鸭！

