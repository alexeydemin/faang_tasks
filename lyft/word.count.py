import fileinput
import heapq
from collections import defaultdict


def run():
    d = defaultdict(lambda: 0)
    for line in fileinput.input():
        for word in line.split():
            d[word] += 1

    for k in sorted(d):
        print(k, d[k])



run()
