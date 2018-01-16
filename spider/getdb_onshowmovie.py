# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 16:27:53 2017

@author: Administrator
"""
import requests,re
import xlwt
 
# 网址
url = "https://movie.douban.com/"
headers = {
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '                            'Chrome/51.0.2704.63 Safari/537.36'
           }
 
req = requests.get(url=url, headers=headers)
 
workbook = xlwt.Workbook(encoding = 'ascii') #创建工作本
worksheet = workbook.add_sheet('My Worksheet') #创建sheet
m = 0
n = 0
for name,score in set(re.findall(r'data-title="(.+?)" .+? data-rate="(.+?)" data-star', req.text)):
    worksheet.write(m, n, name) #写入电影名
    worksheet.write(m, n+1, score) #写入评分
    m += 1
    print (score +'分')
workbook.save('热门电影和评分.xls')
#保存到exl

    
#    try:
#        urllib.request.urlretrieve(link,saveFile(link))
#    except:
#        print('失败')