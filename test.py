#coding:utf8
import cv2
import sys
import multiprocessing
import time
import os
import numpy as np
class imgA:
    def __init__(self):
        print 'init:',os.getpid()
        self.a=[]
        self.b=[]
        self.c=[]
        self.all=[]
        self.radius = multiprocessing.Manager().dict()
        self.radius['a'] = self.a
        self.radius['b']=self.b
        self.radius['c']=self.c
        self.radius['all']=self.all
    def add(self):
        for i in range(self.a.shape[0]):
            for j in range(self.a.shape[1]):
                if(self.a[i][j])>0:
                    self.a[i][j]=0
                else:
                    self.a[i][j]=255
        self.radius['a']=self.a
    def add2(self):
        for i in range(self.b.shape[0]):
            for j in range(self.b.shape[1]):
                if(self.b[i][j])>0:
                    self.b[i][j]=0
                else:
                    self.b[i][j]=255
        self.radius['b']=self.b  #需要更新
    def add3(self):
        for i in range(self.all.shape[0]):
            for j in range(self.all.shape[1]):
                if(self.all[i][j])>0:
                    self.all[i][j]=0
                else:
                    self.all[i][j]=255
        self.radius['all']=self.all  #需要更新
    def read(self):
        self.all=cv2.imread('jingyu.png')
        imgsize=self.all.shape[0]
        self.a = (self.all)[0:imgsize/2]
        self.b = (self.all)[imgsize/2:imgsize]
        self.radius['a'] = self.a
        self.radius['b']=self.b
        self.radius['all']=self.all
if __name__ == '__main__':
    t_ctime=time.clock()
    aa = imgA()
    aa.read()
    print 'start'
    process1 = multiprocessing.Process(target=aa.add, args=())
    process2 = multiprocessing.Process(target=aa.add2, args=())
    process1.daemon = True
    process2.daemon = True
    process1.start()
    process2.start()
    process1.join()
    process2.join()
    print 'done'
    gg=np.concatenate((aa.radius['a'],aa.radius['b']))
    t_ctime=(time.clock()-t_ctime)*1000
    print t_ctime,'ms'
    cv2.imshow('gg',gg)
    cv2.imshow('a',aa.radius['a'])
    cv2.imshow('b',aa.radius['b'])
    cv2.imshow('all',aa.radius['all'])
   # print aa.radius,os.getpid()
    cv2.waitKey(0)
# import cv2
# import numpy as np
# from matplotlib import pyplot as plt
#
# img = cv2.imread('iphone.png',0)
#
# edges = cv2.Canny(img,100,200)
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()