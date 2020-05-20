from typing import List
from collections import Counter


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
        who = set()
        to_whom = []
        for t in trust:
            who.add(t[0])
            to_whom.append(t[1])
        judge, num = Counter(to_whom).most_common(1)[0]
        if judge not in who and N - 1 == num:
            return judge
        return -1


print(Solution.findJudge(None, 2, [[1, 2]]))  # 2
print(Solution.findJudge(None, 3, [[1, 3], [2, 3]]))  # 3
print(Solution.findJudge(None, 3, [[1, 3], [2, 3], [3, 1]]))  # -1
print(Solution.findJudge(None, 3, [[1, 2], [2, 3]]))  # -1
print(Solution.findJudge(None, 4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))  # 3
