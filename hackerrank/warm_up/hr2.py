import math
import os
import random
import re
import sys
from pprint import pprint

# Complete the solve function below.


def solve(a, b):
    res = [0, 0]
    for i, _a in enumerate(a):
        if _a > b[i]:
            res[0] += 1
        if _a < b[i]:
            res[1] += 1
    return res


#if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #a = map(int, raw_input().rstrip().split())
aa = [5, 6, 7]
    #b = map(int, raw_input().rstrip().split())
bb = [3, 6, 10]
result = solve(aa, bb)
print ' '.join(map(str, result))

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()