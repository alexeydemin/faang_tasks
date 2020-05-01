# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math


def get_num(x):
    return int(''.join(ele for ele in x if ele.isdigit()))


def solution(T, R):
    dic = {}
    for i in range(len(T)):
        d = get_num(T[i])
        r = 1 if R[i] == 'OK' else 0
        if d in dic:
            dic[d] *= r
        else:
            dic[d] = r
    pos = 0
    for j in dic:
        if dic[j]:
            pos += 1

    return math.floor(pos * 100 / len(dic))









T = [

]
R = [
]
print(solution(T, R))   #33
