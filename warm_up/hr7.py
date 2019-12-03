#!/bin/python

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    print sum(arr)-max(arr)
    print sum(arr)-min(arr)


a = [1, 2, 3, 4, 5]
miniMaxSum(a)
