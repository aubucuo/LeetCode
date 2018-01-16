# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 08:12:50 2018

@author: Administrator
"""
import tinify , os
from qiniuupload import _uploadpic

tinify.key = "key" #API KEY

def _getpic(path): #获得文件夹pic
    fullname = []
    filename = []
    for name in os.listdir(path):
        fullname.append(os.path.join(path, name))
#        print (type(name))
        filename.append(name)
    #含有文件地址、文件名的列表 生成字典
    d = zip(fullname,filename) 
    dic1 = dict(d)
    piclink = []
    for filepath,name in dic1.items(): #遍历图片并压缩
        #压缩一张图片后返回保存地址
        print ("正在压缩%s！"%name)
        savepath = _tinipic(filepath,name)
        #将这张压缩后的图片上传到七牛云
        print ("上传到七牛云！")
        _uploadpic(savepath,name)
        piclink.append("自己的七牛域名"+name)
    #写入文件外链
    with open('F:/tinipic/aalink.txt','w') as f: #加个aa 可以显示在文件夹前面，容易看到
        for i in piclink:
            f.write(i)
        f.close()
        
def _tinipic(largepic,tinipic):
    savepath = 'F:/tinipic/'+tinipic
    #压缩并保存图片
    source = tinify.from_file(largepic)
    source.to_file(savepath)
    #删除原文件
    os.remove(largepic)
    return savepath
    
if __name__ == '__main__':
    path = 'F:\largepic'
    _getpic(path)
    print ('完成！')

