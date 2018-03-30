#coding:utf8
import subprocess,os,shutil,cv2
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
def get_png_size(png_path):
    commond = 'convert %s -print "%wx%h\n" /dev/null' % png_path
    # print(commond)
    p = subprocess.Popen(commond, stdout=subprocess.PIPE, shell=True)
    # 获取命令行的输出
    png_size = p.stdout.read()
    print(png_size)
    return png_size
def convert_png(png_path):
    png_size = get_png_size(png_path)
    # 获取图片的高和宽
    w,h = png_size.split('x')
    temp_dir = os.path.join(os.getcwd(), 'temp')
    print temp_dir
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    # 切割图片的左上角
    commond = 'convert -crop 800x800+0+0 %s %s' % (png_path,temp_dir+'/top-left.png')
    subprocess.Popen(commond, stdout=subprocess.PIPE, shell=True)
    # 切割右上角
    coord = '800x800+%d+%d' % (int(w)-800,0)
    commond = 'convert -crop %s %s %s' % (coord,png_path, temp_dir + '/top-right.png')
    subprocess.Popen(commond, stdout=subprocess.PIPE, shell=True)
    # 切割左下角
    coord = '800x800+%d+%d' % (0,int(h) - 800)
    commond = 'convert -crop %s %s %s' % (coord, png_path, temp_dir + '/left-bottom.png')
    subprocess.Popen(commond, stdout=subprocess.PIPE, shell=True)
    # 切割右下角
    coord = '800x800+%d+%d' % (int(w) - 800, int(h) - 800)
    commond = 'convert -crop %s %s %s' % (coord, png_path, temp_dir + '/right-bottom.png')
    subprocess.Popen(commond, stdout=subprocess.PIPE, shell=True)
    # 切割左中间
    coord = '800x800+%d+%d' % (int(h)/2 - 800,0)
    commond = 'convert -crop %s %s %s' % (coord, png_path, temp_dir + '/left-center.png')
    subprocess.Popen(commond, stdout=subprocess.PIPE, shell=True)
    # 切割右中间
    coord = '800x800+%d+%d' % (int(w)-800, int(h)/2 - 800)
    commond = 'convert -crop %s %s %s' % (coord, png_path, temp_dir + '/right-center.png')
    subprocess.Popen(commond, stdout=subprocess.PIPE, shell=True)
if __name__ == '__main__':
    # png_path = '/Users/qiyue/myxuni/Github/PNG-Recognition-Transparent/jingyu.png'
    # convert_png(png_path)
    temp_dir = os.path.join(os.getcwd(), 'temp')
    print temp_dir
    # 获取左上角图片的左上角
    img_top_left = cv2.(temp_dir+'/top-left.png',cv2.IMREAD_UNCHANGED)
    a = img_top_left[0:30, 0:30]
    # 获取右上角图片的右上角
    img_top_right = cv2.(temp_dir+'/top-right.png',cv2.IMREAD_UNCHANGED)
    b = img_top_right[0:30, 770:800]
    # 获取左下角图片的左下角
    img_left_bottom = cv2.(temp_dir+'/left-bottom.png',cv2.IMREAD_UNCHANGED)
    c = img_left_bottom[770:800, 0:30]
    # 获取右下角图片的右下角
    img_right_bottom = cv2.(temp_dir+'/right-bottom.png',cv2.IMREAD_UNCHANGED)
    d = img_top_left[770:800, 770:800]
    # 获取左中图片的左上角
    img_left_center = cv2.(temp_dir+'/left-center.png',cv2.IMREAD_UNCHANGED)
    e = img_left_center[0:30, 0:30]
    # 获取右中图片的右上角
    img_right_center = cv2.(temp_dir+'/right-center.png',cv2.IMREAD_UNCHANGED)
    f = img_right_center[0:30, 770:800]
    shutil.rmtree(temp_dir)
    # 读取图片,显示每个像素的rgba值,cv2.IMREAD_UNCHANGED代表显示全部属性,默认是不显示透明度a的值


    # # 左上角
    # a = img[0:30, 0:30]
    # print a
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
    # 分别获取4个角的透明度的值,如果是透明的,就是1,不透明就是0
    a_alpha = check_alpha(a)
    b_alpha = check_alpha(b)
    c_alpha = check_alpha(c)
    d_alpha = check_alpha(d)
    e_alpha = check_alpha(e)
    f_alpha = check_alpha(f)

    # 6个点的透明度相加,0代表6个角都不透明,1代表一个角透明,依次类推
    myalpha = a_alpha + b_alpha + c_alpha + d_alpha + e_alpha + f_alpha
    print myalpha




    cv2.waitKey(0)
