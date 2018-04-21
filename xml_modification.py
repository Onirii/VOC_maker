# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:28:20 2018

@author: liuse
"""
from xml.etree.ElementTree import ElementTree, parse
import os 
import os.path
import numpy as np

xml_path = 'H:/pywork/OD/RUN/Annotations/'
xml_save_path = 'H:/pywork/OD/RUN/Annotations/'


def read_xml(in_path):
    tree = ElementTree()
    tree.parse(in_path)
    return tree

def write_xml(tree, out_path):
    tree.write(out_path, encoding='utf-8', xml_declaration=True)
    

for files in os.walk(xml_path):  
    for file in files[2]:  
        print (file + "-->start!")  
        xml_name = os.path.splitext(file)[0] + '.xml'
        filename = os.path.splitext(file)[0] + '.jpg'
        in_path = xml_path + xml_name
        out_path = xml_save_path + xml_name
        tree = read_xml(in_path)
        
        for item in tree.iterfind('object/name'):
            if item.text == 'small-vehicle':
                item.text = 'vehicle'
            elif item.text == 'oiltank':
                item.text = 'storge-tank'
        for item in tree.iterfind('filename'):
            item.text = filename 
        write_xml(tree, out_path)