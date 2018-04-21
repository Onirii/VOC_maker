# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 16:57:55 2018

@author: liusen
"""
import os
import os.path

ann_path = "H:/pywork/OD/DOTA/train/labelTxt/"
cate_dict_path = "H:/pywork/OD/DOTA/train/catelabelTxt/"
cate_list = ['large-vehicle', 'swimming-pool', 'helicopter','bridge', 
             'plane', 'ship', 'soccer-ball-field', 'basketball-court', 
             'ground-track-field', 'small-vehicle', 'harbor', 
             'baseball-diamond', 'tennis-court', 'roundabout', 'storage-tank']  


for files in os.walk(ann_path):  
    for file in files[2]:
        print (file + "-->start!")
        cate_dict = {}.fromkeys(cate_list, -1)
        filelabel = open(ann_path + file, "r")  
        lines = filelabel.read().split('\n')  
        obj = lines[2:len(lines)-1]
        for i in range(len(obj)):
            obj_split = obj[i].split(' ')
            cate_dict[obj_split[8]] = 1
        f = open(cate_dict_path + file, 'w')
        f.write(str(cate_dict))
        f.close()
        
