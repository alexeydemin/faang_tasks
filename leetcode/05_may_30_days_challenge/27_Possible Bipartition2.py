from collections import defaultdict
from typing import List

class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        color = {}

        def dfs(node, c=1):
            if node in color:
                return int(color[node] == c)
            color[node] = c
            res = 1
            for no in graph[node]:
                res *= dfs(no, c * -1)
            return res

        r = 1
        for node in range(1, N + 1):
            if node not in color:
                r *= dfs(node)
        return bool(r)


print(Solution().possibleBipartition(N=4, dislikes=[[1, 2], [1, 3], [2, 4]]))  # true
print(Solution().possibleBipartition(N=3, dislikes=[[1, 2], [1, 3], [2, 3]]))  # false
print(Solution().possibleBipartition(N=5, dislikes=[[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]]))  # false
