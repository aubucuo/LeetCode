# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 08:55:47 2018

@author: Administrator
"""
# flake8: noqa
from qiniu import Auth, put_file, etag

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


