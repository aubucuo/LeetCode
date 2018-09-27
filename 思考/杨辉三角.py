# -*- coding: utf-8 -*-
'''
在廖雪峰官网看到生成器、迭代器的解释，末尾的练习题动手做一下。
'''

def triangles():
    ls = [1,]
    
    while True:
        n = len(ls)
        while n>0:
            if n-1 :
                ls[n-1]=(ls[n-2]+ls[n-1])
            else:
                ls.append(ls[n-1]+0)
            n -= 1
        yield ls

g = triangles()
next(g)