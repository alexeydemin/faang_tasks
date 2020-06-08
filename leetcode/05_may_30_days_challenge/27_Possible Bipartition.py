from collections import defaultdict
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        conf = defaultdict(list)
        for d in dislikes:
            conf[d[0]].append(d[1])
            conf[d[1]].append(d[0])

        for who in conf:
            #print(who, conf[who])
            li = conf[who]
            for i in range(len(li)-1):
                for j in range(i+1, len(li)):
                     if li[i] in conf[li[j]] or li[j] in conf[li[i]]:
                         return False
        return True


print(Solution.possibleBipartition(None, N=4, dislikes=[[1, 2], [1, 3], [2, 4]]))  # true
print(Solution.possibleBipartition(None, N = 3, dislikes = [[1,2],[1,3],[2,3]])) #false
print(Solution.possibleBipartition(None, N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]])) #false
