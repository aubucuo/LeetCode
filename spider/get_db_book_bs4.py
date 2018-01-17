# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 17:44:30 2018

@author: xglc
找到豆瓣图书的【新书速递】内容
"""
import requests
from bs4 import BeautifulSoup

def _gethtml():
    try:
        req = requests.get('https://book.douban.com/')
        htm = []
        htm.append(req.text)
    except Exception as e:  
        raise e 
    return htm

def _getdata(html):
    title = []
    author = []
    data2 = {} #字典
    soup = BeautifulSoup(html,'html.parser')
    for li in soup.find('ul',attrs={'class':'list-col list-col5 list-express slide-item'}).find_all("li"):
        title.append(li.find('div',class_='info').find('div',class_='title').text)
        author.append(li.find('div',class_='info').find('div',class_='author').text)
    for i in title:
        for j in author:
            data2[i] = j
            break
    return data2

def _txt(data3):
    with open('f://book.txt','w') as f:
        for t,a in data3.items():
            f.write(t+a)
#            for au in data3['author']:
        f.close
        
if __name__ == '__main__':  
    htmls = _gethtml()  
    data = _getdata(htmls[0]) 
    _txt(data) 
#    print (data['title'])