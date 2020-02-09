#!/bin/python

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    _min = 1000000001
    _max = -1
    min_break = 0
    max_break = 0
    for s in scores:
        #print s
        if s > _max:
            _max = s
            max_break += 1
        if s < _min:
            _min = s
            min_break += 1
        #print _min, _max

    if _min == 1000000001:
        _min = 1
    if _max == -1:
        _max = 1

    return max_break-1, min_break-1


print breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])