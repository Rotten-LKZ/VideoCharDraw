## Archived

This project is no longer maintained

# VideoCharDraw

## 中文

#### 介绍

视频字符画

#### 文件

- CharDraw.py 最初版本字符画
- CharDraw_compress.py 带压缩版本字符画
- CharDraw_thread.py 带压缩和多线程版本字符画
- CharDraw_frame 带多线程压缩和抽帧版本字符画

#### 安装教程

1.  直接clone或者下载zip（zip好，多半不会更新了）
2.  下载pillow和opencv-python库（numpy在opencv里面有带，国内建议pip国内镜像）

#### 使用说明

1.  根据最上面提示更改变量
2.  运行

#### 代码详解

1. 引入一些需要的库
2. 获取视频帧数，为导出做准备（除frame）
3. 截取视频所有的帧，之后再一帧一帧转换成字符画
4. 把所有转换成字符画的帧再合并成视频

#### 其他

1. fps计算方法
> **CharDraw_frame.py文件特有的**
> 
> 有两个变量：fps和count
> 
> fps是最终输出的fps数，count是第几帧输出一帧
> 
> 源代码：
>
> ```python
> while True:
> 	...
> 	if a % count == 0:  # 此处a是计算循环执行了多少次，从1开始
> 		# 保存图片
> 		...
> 	...
> ```
> 
> 循环次数取余count等于0就截取一帧
> 
> 那么我有一个30fps的一支视频
> 
> 那么我count可以等于2，fps就是15
> 
> 大概就是这样
> 
2. 输出文件压缩
> *除CharDraw.py原始版本都有的图片压缩*
> 
> 在函数imageToChar里面倒数第三行有一个
>
> ```python
> [cv2.IMWRITE_JPEG_QUALITY, 2]
> ```
> 
> 这个是压缩的格式，后面那个2可以变动，1-100以内    
> 
> 0的话就是死命压缩，只不过画质不太好    
> 
> 如果想要看清楚字符的话可以考虑把这个调高一点，但相对应的    
>
> 输出图片所占硬盘大小也会很高    
3. 如果你不想删除输出的图片的话，把倒数第四行那个daleteImg()给他注释掉就好

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

## English

#### Notice

This English version is mostly Google Translate and cannot guarantee the accuracy of the translation, please refer to Chinese as much as possible, thank you for your understanding

#### Description

Video Char Draw

#### Documentation

- CharDraw.py First version
- CharDraw_compress.py A version with compress
- CharDraw_thread.py A version with compress and thread

#### Installation

1.  Download ZIP or clone(Probably not upgrade)
2.  Download libraries pillow and opencv-python(library numpy will install with opencv)

#### Instructions

1.  Modify the variables as indicated above
2.  Run code

#### Code details

1. Introduce some required libraries
2. Get the number of video frames to prepare for export (except frame)
3. Intercept all the frames of the video, and then convert them frame by frame to character painting
4. Combine all the frames converted into character paintings and merge them into video

#### Other

1. fps calculation method
> **fps just in CharDraw_frame.py**
> 
> There are two variables: fps and count
> 
> fps is the number of FPS of the final output, count emmm......
> 
> There is source code:
> 
> ```python
> a = 0
> while True:
> 	a += 1
> 	if a % count == 0:
> 		# save image
> 		...
> 	...
> ```
2. Output file compression
> The third to last line in function imageToChar
> 
> ```python
> [cv2.IMWRITE_JPEG_QUALITY, 2]
> ```
> 
> You can change the 2 to 0-100
> 
> If you want to see the characters clearly, you can consider raising this a little bit, but the corresponding
> 
> The output image will also take up a large amount of hard disk size
3. If you do n’t want to delete the output image, comment out the daleteImg () on the penultimate line

#### Contribution

1.  Fork the repository
2.  Create Feat_xxx branch
3.  Commit your code
4.  Create Pull Request
