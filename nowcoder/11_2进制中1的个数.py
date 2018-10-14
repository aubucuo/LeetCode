# -*- coding:utf-8 -*-
'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
class Solution:
    def NumberOf1(self, n):
        # write code here
        flag=1
        print(type(flag))
        count=0
        maxBit=32
        for i in range(maxBit):
            if n & flag:
                count+=1
            flag=flag<<1
        return count