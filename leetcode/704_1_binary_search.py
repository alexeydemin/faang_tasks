from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1



print(Solution.search(None, nums=[-1, 0, 3, 5, 9, 12], target=9))  # 4
print(Solution.search(None, nums=[-1, 0, 3, 5, 9, 12], target=2))  # -1
