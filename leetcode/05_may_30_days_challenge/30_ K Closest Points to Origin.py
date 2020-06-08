from typing import List
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        for p in points:
            heapq.heappush(h, (p[0] ** 2 + p[1] ** 2, p))

        return [x[1] for x in heapq.nsmallest(K, h)]


# print(Solution().kClosest(points=[[1, 3], [-2, 2]], K=1))  # [-2,2]]
print(Solution().kClosest(points=[[3, 3], [5, -1], [-2, 4]], K=2))  # [[3,3],[-2,4]]
