#!/bin/python

import math
import os
import random
import re
import sys


# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return 'YES'
        else:
            return 'NO'
    else:
        t = float(x2 - x1) / float(v1 - v2)
        if t > 0 and t.is_integer():
            return 'YES'
        else:
            return 'NO'


# kangaroo(1,2,3,4)
# kangaroo(0, 3, 4, 2)
# kangaroo(21, 6, 47, 3)
print kangaroo(43, 2, 70, 2)
