from typing import List


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for i, n in enumerate(nums):
            if target == n:
                res.append(i)

        return sorted(res)


print(Solution.targetIndices(None, nums=[1, 2, 5, 2, 3], target=2))
print(Solution.targetIndices(None, nums=[1, 2, 5, 2, 3], target=3))
print(Solution.targetIndices(None, nums=[1, 2, 5, 2, 3], target=5))
