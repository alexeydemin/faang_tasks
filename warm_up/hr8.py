#!/bin/python

import math
import os
import random
import re
import sys


# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max = 0
    num = 0
    for i in ar:
        if i > max:
            max = i
            num = 1
            continue
        if i == max:
            num += 1
    return num


a = [3, 2, 1, 3]
print birthdayCakeCandles(a)
