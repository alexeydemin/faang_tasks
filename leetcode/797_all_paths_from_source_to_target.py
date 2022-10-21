from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(cur, path):
            if cur == len(graph) - 1:
                res.append(path)
            else:
                for i in graph[cur]:
                    dfs(i, path + [i])

        res = []
        dfs(0, [0])
        return res


print(Solution.allPathsSourceTarget(Solution, graph=[[1, 2], [3], [3], []]))
# [[0,1,3],[0,2,3]]


print(Solution.allPathsSourceTarget(Solution, graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
# [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
