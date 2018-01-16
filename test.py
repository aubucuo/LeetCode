# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 08:36:06 2018

@author: Administrator
"""

import os

listpic = []    #全局变量，存放符合要求的图片

def getallpic(path):
   for name in os.listdir(path):
       fullname = os.path.join(path, name)
       if os.path.isdir(fullname):      #判断是否为文件夹
           getallpic(fullname)     #递归遍历文件
       elif os.path.isfile(fullname):    #判断是否是文件
           filename, ext = os.path.splitext(fullname)    #获取扩展名
           try :
               if ext.lower() == '.png':
                   listpic.append(fullname)
                   print (os.system('optipng '+ fullname) )   #使用optipng
               elif ext.lower() == '.jpg':
                   listpic.append(fullname)
                   print (os.system('jpegoptim '+ fullname) )   #使用jpegoptim
               else :
                   pass
           except Exception as e:
               print ('can not compress this picture ' + e)
       else :
           print
   return listpic

if __name__ == '__main__':
   path = '/home/pwprice/work/static/'
   li = getallpic(path)
   print (li)    #打印出所有符合要求的图片
   print (len(li) )   #计算列表长度