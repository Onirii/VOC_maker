# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:36:48 2018

@author: liuse
"""

#import re  
import os  
import time  
#str.split(string)分割字符串  
#'连接符'.join(list) 将列表组成字符串  
def change_name(path):  
    global i  
    if not os.path.isdir(path) and not os.path.isfile(path):  
        return False  
    if os.path.isfile(path):  
        file_path = os.path.split(path) #分割出目录与文件  
        lists = file_path[1].split('.') #分割出文件与文件扩展名  
        file_ext = lists[-1] #取出后缀名(列表切片操作)  
        img_ext = ['bmp','jpeg','gif','psd','png','jpg','txt', 'xml']  
        if file_ext in img_ext:  
            os.rename(path,file_path[0]+'/'+'0'*(6-len(str(start_num+ i*2))) + str(start_num+ i*2)+'.jpg')  
            i += 1  #注意这里的i是一个陷阱  
        #或者  
        #img_ext = 'bmp|jpeg|gif|psd|png|jpg'  
        #if file_ext in img_ext:  
        #    print('ok---'+file_ext)  
    elif os.path.isdir(path):  
        for x in os.listdir(path):  
            change_name(os.path.join(path,x)) #os.path.join()在路径处理上很有用  
img_dir = 'H:/pywork/OD/UCAS/VOCUCAS/J' 
#img_dir = img_dir.replace('\\','/')  
start = time.time()  
start_num = 2810
i = 0  
change_name(img_dir)  
c = time.time() - start  
print('程序运行耗时:{:.2f}'.format(c))  
print('总共处理了{:.0f}张图片'.format(i))  