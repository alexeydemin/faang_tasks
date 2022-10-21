from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        map = defaultdict(list)
        indegree = defaultdict(int)
        for dest, src in prerequisites:
            map[src].append(dest)
            indegree[dest] += 1
        zero_stack = set()
        for course in range(numCourses):
            if course not in indegree:
                zero_stack.add(course)

        res = []
        while zero_stack:
            vert = zero_stack.pop()
            res.append(vert)
            if vert in map:
                for peer in map[vert]:
                    indegree[peer] -= 1
                    if indegree[peer] == 0:
                        zero_stack.add(peer)
        return res if numCourses == len(res) else []


print(Solution.findOrder(None, numCourses=4, prerequisites=[[1, 0], [2, 0], [3, 1], [3, 2]]))
# [0,2,1,3] or [0,1,2,3]

print(Solution.findOrder(None, numCourses=1, prerequisites=[]))
# [0]


# dest src
# [1, 0]
# [2, 0]
# [3, 1]
# [3, 2]
