#!/bin/python

from __future__ import print_function

import os
import sys


def getTotalX(a, b):
    res = 0
    lena = len(a)
    lenb = len(b)
    mula = 1
    mulb = 1
    for ai in a:
        mula *= ai
    for bi in b:
        mulb *= bi
    for i in range(2, 101):
        if pow(i, lena, mula*lena) == 0 and mulb % pow(i, lenb) == 0:
            res += 1
    return res


#print (getTotalX([2, 6], [24, 36]))
#print (getTotalX([2, 4], [16, 32, 96]))
print (getTotalX([3, 4], [24, 48]))


