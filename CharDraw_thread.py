from cv2 import cv2
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import threading

video_path = "videott.mp4"  # 视频路径
out_path = "out/"  # 输出目录
huaZhi = 2  # 清晰度，最低1，无上限

# -----以下为程序使用变量-----#
video_info = []

num = 0

info = []
'''
图片转换成字符里面的相关大小，
为元组，第一个是resize的宽高，第二个是图片输出的宽高
'''

video = cv2.VideoCapture(video_path)


# 获取视频信息
def getVideoInfo() -> list:
    ret = []

    (major_ver, minor_ver, subminor_ver) = cv2.__version__.split('.')
    if int(major_ver) < 3:
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = video.get(cv2.CAP_PROP_FPS)

    ret.append(fps)  # 视频帧数
    ret.append(video.read()[1].shape[0])  # 视频高度
    ret.append(video.read()[1].shape[1])  # 视频宽度
    return ret


# 获取视频所有截图
def outVideoAllCapture():
    # 判断载入视频是否可以打开
    ret = video.isOpened()
    global num
    # 循环读取视频帧
    while ret:
        num = num + 1
        # 进行单张图片的读取,ret的值为True或者Flase,frame表示读入的图片
        ret, frame = video.read()
        if ret:
            cv2.imwrite(out_path + str(num) + '.jpg', frame)
            cv2.waitKey(1)
        else:
            break
    # mergeImage()


# 单张图片转换成字符画
def imageToChar(filename, number):
    # 字符列表
    ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/|()1{}[]?-_+~            <>i!lI;:,\"^`'. ")
    # 判断图片是否存在
    if os.path.exists(filename):
        # 将图片转化为灰度图像,并重设大小
        img_array = np.array(Image.open(filename).resize(info[0], Image.ANTIALIAS).convert('L'))  # resize里面 宽, 高 输出宽高/7
        # 创建新的图片对象
        img = Image.new('L', info[1], 255)  # 宽, 高
        draw_object = ImageDraw.Draw(img)
        # 设置字体
        font = ImageFont.truetype('consola.ttf', 10, encoding='unic')
        # 根据灰度值添加对应的字符
        for j in range(info[0][1]):  # 是resize的高
            for k in range(info[0][0]):  # 宽
                x, y = k * 8, j * 8
                index = int(img_array[j][k] / 4)
                draw_object.text((x, y), ascii_char[index], font=font, fill=0)
        # 保存字符图片
        img.save(out_path + str(number) + "g.jpg", 'JPEG')
        cv2.imwrite(out_path + str(number) + "g.jpg", cv2.imread(out_path + str(number) + "g.jpg"),
                    [cv2.IMWRITE_JPEG_QUALITY, 2])
        os.remove(out_path + str(number) + '.jpg')  # 删除原始图片
        print("已成功把第" + str(number) + "帧转换成字符画")


def mergeImage():
    print("开始将图片合并成MP4视频")
    # global num
    videoWriter = cv2.VideoWriter(out_path + 'out.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), video_info[0],
                                  info[1])
    for i in range(1, num + 1):
        filename = out_path + str(i) + 'g.jpg'
        if os.path.exists(filename):
            img = cv2.imread(filename=filename)
            cv2.waitKey(100)
            videoWriter.write(img)
    print("完成图片合并成MP4视频")


def deleteImg():
    print("开始删除转换图片")
    global num
    for i in range(1, num + 1):
        os.remove(out_path + str(i) + 'g.jpg')
    print("删除转换图片完毕")


class NewTransform(threading.Thread):
    def __init__(self, thread_id: int, name: str, is_first: bool):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.first = is_first

    def run(self):
        print("开始线程：", self.thread_id)
        # print(self.first)
        # print(num)
        if self.first:
            for i in range(1, int((num + 1) / 2)):
                # print(int(num / 2))
                imageToChar(out_path + str(i) + '.jpg', i)
        else:
            for i in range(int((num + 1) / 2), num + 1):
                # print(num - int(num / 2))
                imageToChar(out_path + str(i) + '.jpg', i)

        print("结束线程：", self.thread_id)


if __name__ == "__main__":
    # os.makedirs(out_path)
    if not os.path.exists(out_path):
        os.makedirs(out_path)
    video_info = getVideoInfo()
    info.append((int(video_info[2] * huaZhi / 8), int(video_info[1] * huaZhi / 8)))
    info.append((int(video_info[2] * huaZhi / 8) * 8, int(video_info[1] * huaZhi / 8) * 8))
    print(info)

    outVideoAllCapture()  # 截取视频所有帧

    thread_1 = NewTransform(1, "Last", True)
    thread_2 = NewTransform(2, "Next", False)
    thread_1.start()
    thread_2.start()
    thread_1.join()
    thread_2.join()
    mergeImage()
    deleteImg()  # 删除每一帧的字符画

video.release()
