# -*- coding:utf-8 -*-
'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return 0
        elif base == 1:
            return 1
        elif exponent == 0:
            return 1
        elif exponent == 1:
            return base
        else:
            return pow(base, exponent)