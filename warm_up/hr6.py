#!/bin/python

import math
import os
import random
import re
import sys


def staircase(n):
    s = ''
    for i in range(0, n):
        s += '#'
        print ('{0: >' + str(n) + '}').format(s)


staircase(10)
