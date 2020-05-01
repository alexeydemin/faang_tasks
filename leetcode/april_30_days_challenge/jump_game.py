from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx = 0
        for i in range(len(nums)):
            if i > mx:
                return False
            else:
                mx = max(mx, i + nums[i])
        return True

#print(Solution.canJump(None, [2, 5, 0, 0, 3, 0, 0, 6, 0, 0, 0, 1]))  # True
#print(Solution.canJump(None, [2, 3, 1, 1, 4]))  # True
print(Solution.canJump(None, [3, 2, 1, 0, 4]))  # False
