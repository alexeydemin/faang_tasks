from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = []
        dic = {}
        mx = 0
        s = 0
        for n in nums:
            s += 1 if n else -1
            counts.append(s)
        for i, c in enumerate(counts):
            if c not in dic:
                dic[c] = i
            else:
                mx = max(i - dic[c], mx)
            if c == 0:
                mx = max(mx, i + 1)
        return mx


# print(Solution.findMaxLength(None, [0, 1, 0]))
# print(Solution.findMaxLength(None, [1, 0, 1, 1, 0, 1, 1, 1, 0]))
print(Solution.findMaxLength(None, [1, 1]))
