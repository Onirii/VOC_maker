# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 09:49:20 2018

@author: liusen
"""
from xml.etree.ElementTree import parse
import os  
import os.path  
from PIL import Image
import numpy as np
import scipy
  
im_path = "H:/pywork/OD/DOTA/JPEGImages/"  
xml_path = "H:/pywork/OD/DOTA/Annotations/" 
back_path = 'H:/pywork/OD/DOTA/Backgrounds/'
#max_pixel = int(89398440)

def image_resize(fileimpath, im_name, max_size_index, max_size):
    if max_size_index == 0:
        im_back_data = np.zeros((int(np.floor(max_size/2)), max_size, 3))
    else:
        im_back_data = np.zeros((max_size, int(np.floor(max_size/2)), 3))
    scipy.misc.imsave(back_path + im_name, im_back_data)
    im = Image.open(fileimpath)
    im_back = Image.open(back_path + im_name)
    im_back.paste(im, (0, 0))
    im_back.save(back_path + im_name)

    
def xml_parse(filexmlpath):
    data = parse(filexmlpath)
    for item in data.iterfind('size'):
        width = item.findtext('width')
        height = item.findtext('height')
    wh_ratio = int(width) / int(height)
    #hw_ratio = int(height) / int(width)
    if 0.5<wh_ratio<2:
        max_size = None
        max_size_index = None
    else:
        list_0 = [int(width), int(height)]
        max_size = max(list_0)
        max_size_index = list_0.index(max(list_0))
    return max_size_index, max_size
           
for files in os.walk(im_path):  
    for file in files[2]:  
        print (file + "-->start!")  
        xml_name = os.path.splitext(file)[0] + '.xml'
        im_name = os.path.splitext(file)[0] + '.png'
        filexmlpath = xml_path + xml_name
        fileimpath = im_path + im_name 
        try:
            max_size_index, max_size = xml_parse(filexmlpath)
            if max_size:
                image_resize(fileimpath, im_name, max_size_index, max_size)
        except FileNotFoundError:
            print('no such file!')
        except MemoryError:
            print('This picture is strange' , im_name)