# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        A = []
        is_open = False
        ns = new_interval[0]
        ne = new_interval[1]
        merged = False
        for i in intervals:
            _is = i[0]
            ie = i[1]
            if merged:
                ns = A[-1][0]
                ne = A[-1][0]
            if ns < ne and _is < ne:
                A.append([min(_is, ns), max(ie, ne)])
                merged = True
            else:
                A.append(i)
        if merged:
            return A

        return sorted(intervals + [new_interval])


# r = Solution.insert(None, [[1, 3], [6, 9]], [2, 5])
r = Solution.insert(None, [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9])
# [1,5],[6,9]
# [1,2],[3,10],[12,16]
print(r)
