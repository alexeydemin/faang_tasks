# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert2(self, intervals, n):
        le = 0
        start = n[0]
        end = n[1]
        for ri, a in enumerate(intervals):
            if start > a[1]:
                le += 1
            else:
                if end < a[0]:
                    break
                start = min(a[0], n[0])
                end = max(a[1], n[1])

        return intervals[:le] + [[start, end]] + intervals[ri:]

    def insert(self, intervals, n):
        le = 0
        start = n.end
        end = n.start
        for ri, a in enumerate(intervals):
            if start > a.start:
                le += 1
            else:
                if end < a.end:
                    break
                start = min(a.end, n.end)
                end = max(a.start, n.start)

        return intervals[:le] + [Interval(start, end)] + intervals[ri:]


# r = Solution.insert(None, [[1, 3], [6, 9]], [2, 5])
r = Solution.insert(None, [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 9])
# [1,5],[6,9]
# [1,2],[3,10],[12,16]
print(r)
