#coding:utf8
import cv2
import numpy as np

# 把二维的列表转化成一维的列表,并去重
def new_list(mylists):
    new_lists = []
    for mylist in mylists:
        for i in mylist:
            if i not in new_lists:
                new_lists.append(i)
    return new_lists
# 检测像素块的透明通道是否为0,是0就返回1,不是0就返回0  (0代表透明的意思)
def check_alpha(myndarray):
    # 获取每个像素的alpha的值(代表透明度)
    alpha = myndarray[:, :, 3]
    # 把多维数组转化为列表
    alpha_list = np.ndarray.tolist(alpha)
    # 把多维列表里的元素去重,转化成一维的列表
    alpha_list_new = new_list(alpha_list)
    # 判断列表的值,如果列表为[0],就代表全是透明的,返回1,否则返回0
    if alpha_list_new == [0]:
        return 1
    else:
        return 0
if __name__ == '__main__':
    import os,shutil
    print os.getcwd()
    temp_dir = os.path.join(os.getcwd(), 'temp')
    print temp_dir
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    # img = cv2.imread("opaque.png", cv2.IMREAD_UNCHANGED)
    # img = cv2.imread("transparent.png", cv2.IMREAD_UNCHANGED)
    # img = cv2.imread("iphone.png", cv2.IMREAD_UNCHANGED)
    # img = cv2.imread("bird.png", cv2.IMREAD_UNCHANGED)
    # 读取图片,显示每个像素的rgba值,cv2.IMREAD_UNCHANGED代表显示全部属性,默认是不显示透明度a的值
    # im = cv2.imread('jingyu_crop.png',0)
    # sp = im.shape
    # print sp
    # from PIL import Image
    #
    # magick convert /Users/qiyue/myxuni/Github/PNG-Recognition-Transparent/kisspng-gratis-computer-file-beautiful-border-5a9ac023ce03c7.9815606115200911718439.jpg  /Users/qiyue/myxuni/Github/PNG-Recognition-Transparent/kisspng-gratis-computer-file-beautiful-border-5a9ac023ce03c7.9815606115200911718439.png
    # convert -crop 800x800+0+0 jingyu.png jingyu01.png
    # convert  /Users/qiyue/myxuni/Github/PNG-Recognition-Transparent/jingyu.png  -crop 10x50 /Users/qiyue/myxuni/Github/PNG-Recognition-Transparent/jingyu1.png
    img = cv2.imread("jingyu.png", cv2.IMREAD_UNCHANGED)
    img1 = cv2.imread("jingyu01.png", cv2.IMREAD_UNCHANGED)
    img2 = cv2.imread("jingyu01.png", cv2.IMREAD_UNCHANGED)
    img3 = cv2.imread("jingyu01.png", cv2.IMREAD_UNCHANGED)
    img4 = cv2.imread("jingyu01.png", cv2.IMREAD_UNCHANGED)
    img5 = cv2.imread("jingyu01.png", cv2.IMREAD_UNCHANGED)
    sp = img.shape
    print sp
    # print type(img)
    print img
    # # 获取图片的大小(长,宽,属性(4代表显示rgba,3代表rgb))
    # 图片的高
    h = sp[0]
    # 图片的宽
    w = sp[1]
    # 下面是获取图片的四个角的像素块
    # for h in range(0, 5):
    #     for w in range(0, 5):
    #         pixel = img.getpixel((w, h))
    #         print pixel
    # 左上角
    a = img[0:30, 0:30]
    print a
    # 左下角
    b = img[h-30:h, 0:30]
    # 右下角
    c = img[h-30:h, w-30:w]
    # 右上角
    d = img[0:30, w-30:w]
    # 左侧中间
    e = img[h/2-30:h/2,0:30]
    # 右侧中间
    f = img[h / 2 - 30:h / 2, w - 30:w]
    # 分别获取4个角的透明度的值,如果是透明的,就是1,不透明就是0
    a_alpha = check_alpha(a)
    b_alpha = check_alpha(b)
    c_alpha = check_alpha(c)
    d_alpha = check_alpha(d)
    e_alpha = check_alpha(e)
    f_alpha = check_alpha(f)
    # cv2.imshow("e",e)
    # cv2.imshow("e",f)
    # cv2.waitKey(0)


    # 4个角的透明度相加,0代表4个角都不透明,1代表一个角透明,依次类推
    myalpha = a_alpha + b_alpha + c_alpha + d_alpha + e_alpha + f_alpha
    print myalpha

    # from PIL import Image
    # import matplotlib.pyplot as plt
    #
    # img = Image.open('jingyu.png')  # 打开图像
    # plt.figure("beauty")
    # plt.subplot(1, 2, 1), plt.title('origin')
    # plt.imshow(img), plt.axis('off')
    #
    # box = (80, 100, 260, 300)
    # roi = img.crop(box)
    # plt.subplot(1, 2, 2), plt.title('roi')
    # plt.imshow(roi), plt.axis('off')
    # plt.show()


    # h = sp[0]
    # # 图片的宽
    # w = sp[1]
    # # 下面是获取图片的四个角的像素块
    # # 左上角
    # a = img[0:30, 0:30]
    # # 左下角
    # b = img[h-30:h, 0:30]
    # # 右下角
    # c = img[h-30:h, w-30:w]
    # # 右上角
    # d = img[0:30, w-30:w]
    # # 左侧中间
    # e = img[h/2-30:h/2,0:30]
    # # 右侧中间
    # f = img[h / 2 - 30:h / 2, w - 30:w]
    # # 分别获取4个角的透明度的值,如果是透明的,就是1,不透明就是0
    # a_alpha = check_alpha(a)
    # b_alpha = check_alpha(b)
    # c_alpha = check_alpha(c)
    # d_alpha = check_alpha(d)
    # e_alpha = check_alpha(e)
    # f_alpha = check_alpha(f)
    #
    # # 4个角的透明度相加,0代表4个角都不透明,1代表一个角透明,依次类推
    # myalpha = a_alpha + b_alpha + c_alpha + d_alpha + e_alpha + f_alpha
    # print myalpha
    cv2.waitKey(0)
# cv2.imshow("a",a)
# cv2.imshow("b",b)
# # cv2.imshow("c",c)
# cv2.imshow("d",d)
# cv2.waitKey(0)