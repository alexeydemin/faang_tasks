# t1 = [1, 18, 5, 3, 16]
# t2 = [4, 12, 19, 2, 5]
# t3 = [2, 7, 20, 9, 1]
# t4 = [4, 17, 12, 4, 8]
#
# t = [t1, t2, t3, t4]
#
#
# [
# [1,3,5,16,18],
# [19, *12, 5, 4, 2]
# [2, 1, *7, 9, 20]
# [*17, 12, 8, 4, 4]
# ]

def srt(t, last_floor, dir, changes):
    below = []
    upper = []
    for i in t:
        below.append(i) if i <= last_floor else upper.append(i)

    upper_ask = sorted(upper)
    below_desc = sorted(below, reverse=True)
    if len(upper_ask) and len(below_desc):
        changes += 1
    result_list = below_desc + upper_ask if dir else upper_ask + below_desc
    print(result_list, changes)
    return result_list, result_list[-1], 1 - dir, changes


def solution(times):
    last_floor = 0
    dir = 1
    res = []
    changes = 0
    for time in times:
        sorted_time, last_floor, dir, changes = srt(time, last_floor, dir, changes)
        res.append(sorted_time)
    return res, changes


t1 = [1, 18, 5, 3, 16]
t2 = [4, 12, 19, 2, 5]
t3 = [2, 7, 20, 9, 1]
t4 = [4, 17, 12, 4, 8]
t5 = [4, 7, 8, 9, 10]
# t2 = [21, 20, 19, 25, 26]
# t3 = [25, 24, 23, 22, 21]
# t4 = [20, 18, 17, 16, 14]
t = [t1, t2, t3, t4, t5]

r = solution(t)
print(r)
