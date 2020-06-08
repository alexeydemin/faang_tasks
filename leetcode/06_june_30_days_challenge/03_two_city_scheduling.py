from typing import List
import heapq


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        h = []
        for p in costs:
            heapq.heappush(h, (int(p[0] - p[1]), p))
        a = heapq.nsmallest(n, h)
        b = heapq.nlargest(n, h)
        a_sum = b_sum = 0
        for i in range(n):
            a_sum += a[i][1][0]
            b_sum += b[i][1][1]
        return a_sum + b_sum


print(Solution().twoCitySchedCost([[10, 20], [30, 200], [400, 50], [30, 20]]))  # 110
