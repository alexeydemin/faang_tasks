from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        for f in firstList:
            for s in secondList:
                if s[0] <= f[1] and s[1] >= f[0] or f[0] <= s[1] and f[1] >= s[0]:
                    res.append([max(s[0], f[0]), min(s[1], f[1])])
                elif f[1] < s[0]:
                    break
print(Solution.intervalIntersection(None,
                                    firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                                    secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]
                                    )
      )
# [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]))
