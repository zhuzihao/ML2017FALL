# -*- coding: utf-8 -*-
"""
Created on Tue May 22 19:39:19 2018

@author: zihaozhu
"""
words=[]
fp = open("words.txt","r")
content = fp.read().split()
count = 0
for word in content:
    if word not in words:
        print(word+" "+str(count)+" "+str(content.count(word)))
        words.append(word)
    count = count + 1