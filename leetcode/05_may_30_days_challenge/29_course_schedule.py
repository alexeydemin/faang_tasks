from typing import List
from collections import defaultdict


class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        vs = set()
        for p in prerequisites:
            graph[p[0]].append(p[1])
            vs.add(p[0])
            vs.add(p[1])
        graph = dict(graph)
        visited = {}
        st = {}

        def has_loop(vt):
            visited[vt] = True
            st[vt] = True
            if vt in graph:
                for peer in graph[vt]:
                    if peer not in visited:
                        if has_loop(peer):
                            return True
                    elif peer in st:
                        return True
            del st[vt]
            return False

        for v in vs:
            if v not in visited:
                if has_loop(v):
                    return False
        return True


print(Solution().canFinish(n=8, prerequisites=[[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]))  # x
print(Solution().canFinish(n=3, prerequisites=[[0, 1], [0, 2], [2, 1]])) #True
print(Solution().canFinish(n=2, prerequisites=[[1, 0]])) #True
print(Solution().canFinish(n=2, prerequisites=[[1, 0], [0, 1]])) #False
print(Solution().canFinish(n=2, prerequisites=[[2, 3], [3, 2]])) #False
