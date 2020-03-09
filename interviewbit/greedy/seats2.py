class Solution:
    def seats(self, s):
        arr = list(s)
        # 1. count center
        su = 0
        n = 0
        for i, a in enumerate(arr):
            if a == 'x':
                su += i
                n += 1
        if not n:
            return 0
        center = round(su / n)
        [start, end] = Solution.getStartEnd(self, center, arr)
        i = 0
        # 0123456789
        # ..xx.x
        hops = 0
        while i < len(arr):
            if arr[i] == 'x':
                if i <= center and i < start:
                    if start is False:
                        hops += center - i
                        arr[center] = 'x'
                    else:
                        hops += start - i - 1
                        arr[start - 1] = 'x'
                else:
                    if i > end:
                        if end is False:
                            hops += center - i
                            arr[center] = 'x'
                        else:
                            hops += i - end - 1
                            arr[end + 1] = 'x'
            i += 1
            [start, end] = Solution.getStartEnd(self, center, arr)
        return hops
        return res % 10000003

    def getStartEnd(self, center, arr):
        if arr[center] != 'x':
            return [False, False]
        stop_start = False
        start = center
        end = center
        stop_end = False
        i = 0
        while True:
            i += 1
            if not stop_start:
                if center - i < 0 or arr[center - i] != 'x':
                    stop_start = True
                else:
                    start = center - i
            if not stop_end:
                if center + i >= len(arr) or arr[center + i] != 'x':
                    stop_end = True
                else:
                    end = center + i
            if stop_start and stop_end:
                return [start, end]


# .x.x.x..x
# 012345678
# ....x..xx...x..
# 012345678901234
# ....x..xx...xxx
# 012345678901234

#r = Solution.seats(None, '.x.x,x..x')
#r = Solution.seats(None, '........')
#r = Solution.seats(None, '..xx.x')
#r = Solution.seats(None, '....x..xx...x..')
                         #123456789012345
r = Solution.seats(None, 'x.x')
# 012345
# s = 'xxxxxx'
# r = Solution.getStartEnd(None, 1, list(s))
print(r)
