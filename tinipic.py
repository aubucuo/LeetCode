# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 08:12:50 2018

@author: Administrator
"""
import tinify , os
from qiniu import Auth, put_file, etag

tinify.key = "替换"

#需要填写你的 Access Key 和 Secret Key
access_key = '替换'
secret_key = '替换'
#构建鉴权对象
q = Auth(access_key, secret_key)
#要上传的空间
bucket_name = '替换'
    
def _uploadpic(filepath,key):
    #key是上传之后的文件名
    #生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    ret, info = put_file(token, key, filepath)
#    print(info)
    assert ret['key'] == key
    assert ret['hash'] == etag(filepath)
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
        piclink.append("替换"+name) #七牛云外链
    #写入文件外链
    with open('F:/tinipic/aalink.txt','a') as f:
        n = 0
        for i in piclink:
            f.write('\n'+i)
            n += 1
        f.write("\n本次%d张图片.END"%n)
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
   
