# PaddleHub 之 一键带你登上《TIME》时代周刊封面

生成对抗网络(Generative Adversarial Network\[[1](#参考文献)\], 简称GAN) 是一种非监督学习的方式，通过让两个神经网络相互博弈的方法进行学习，该方法由lan Goodfellow等人在2014年提出。生成对抗网络由一个生成网络和一个判别网络组成，生成网络从潜在的空间(latent space)中随机采样作为输入，其输出结果需要尽量模仿训练集中的真实样本。判别网络的输入为真实样本或生成网络的输出，其目的是将生成网络的输出从真实样本中尽可能的分辨出来。而生成网络则尽可能的欺骗判别网络，两个网络相互对抗，不断调整参数。
生成对抗网络常用于生成以假乱真的图片。此外，该方法还被用于生成影片，三维物体模型等。\[[2](#参考文献)\]

---
## 内容

- [背景](#背景)
- [结果](#结果)
- [思路](#思路)
- [步骤](#步骤)

## 背景



本项目的目录结构如下：
```
├── time.py 主程序
│ 
├── trainer 不同模型的训练脚本
│   ├── CGAN.py Conditional GAN的训练脚本
│   ├── ...
│   ├── STGAN.py STGAN的训练脚本

```

## 结果

### 安装说明
**安装[PaddlePaddle](https://github.com/PaddlePaddle/Paddle)：**

在当前目录下运行样例代码需要PadddlePaddle Fluid的v.1.7.1或以上的版本。如果你的运行环境中的PaddlePaddle低于此版本，请根据[安装文档](https://www.paddlepaddle.org.cn/documentation/docs/zh/1.5/beginners_guide/install/index_cn.html)中的说明来更新PaddlePaddle。

其他依赖包：
#安装paddlehub中人像抠图的预训练模型

!hub install deeplabv3p_xception65_humanseg

#DeepLabv3+ 是Google DeepLab语义分割系列网络的最新作，其前作有 DeepLabv1, DeepLabv2, DeepLabv3。
#在最新作中，作者通过encoder-decoder进行多尺度#信息的融合，同时保留了原来的空洞卷积和ASSP层， 
#其骨干网络使用了Xception模型，提高了语义分割的健壮性和运行速率，在 PASCAL VOC 2012 dataset取得新的state-of-art performance。
#该PaddleHub Module使用百度自建数据集进行训练，可用于人像分割，支持任意大小的图片输入。

### 任务简介


### 数据准备



### 模型训练




## 思路
### 背景介绍


## 步骤
