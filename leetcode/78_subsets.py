from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            temp = []
            for r in res:
                temp.append(r + [num])
            res += [temp]
        return res


print(Solution.subsets(None, nums=[1, 2, 3]))
# []
# [] + 1
# [] + 1 + 2
