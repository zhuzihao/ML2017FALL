# -*- coding: utf-8 -*-
"""
Created on Tue May 22 20:58:49 2018

@author: zihaozhu
"""

from PIL import Image
im = Image.open("westbrook.jpg") 
out = im.point(lambda i: i // 2)
out.save("new.jpg",quality=100)