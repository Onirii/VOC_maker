# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 09:47:49 2018

@author: liusen
"""
import os

def set_distribution(test_file_path, set_file_path):
    file = open(set_file_path, 'w')
    file_name_list = []
    if os.path.isdir(test_file_path):
        for filename in os.listdir(test_file_path):
            file_name_list.append(int((filename.split('.')[0])))
        #for filename in os.listdir(val_file_path):
            #file_name_list.append(int(filename.split('.')[0]))
        file_name_list_0 = sorted(file_name_list)
        print(len(file_name_list))
        #print(type(file_name_list))
        #print(type(file_name_list_0))
        for _ in range(len(file_name_list)):
            elem = str(file_name_list_0.pop(0))
            file.write('0'*(6-len(elem))+elem+'\n')
        file.close()
        
test_file_path = 'H:/pywork/OD/DOTA/test/images/images'
val_file_path = 'H:/pywork/OD/DOTA/val/images/images'
set_file_path = 'H:/pywork/OD/DOTA/ImageSets/test.txt'
set_distribution(test_file_path, set_file_path)