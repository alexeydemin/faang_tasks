from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(nums, start, end, target):
            if start > end:
                return -1
            mid = (start + end) // 2

            if target < nums[0] and nums[mid] < nums[0] or target >= nums[0] and nums[mid] >= nums[0]:
                comparisor = nums[mid]
            else:
                if target < nums[0]:
                    comparisor = float('-inf')
                else:
                    comparisor = float('inf')

            if comparisor == target:
                return mid
            elif comparisor < target:
                return bs(nums, mid + 1, end, target)
            else:
                return bs(nums, start, mid - 1, target)

        return bs(nums, 0, len(nums) - 1, target)

        # for i, n in enumerate(nums):
        #     if target == n:
        #         return i
        # return -1


print(Solution.search(None, nums=[4, 5, 6, 7, 0, 1, 2], target=0))  # 4
print(Solution.search(None, nums=[4, 5, 6, 7, 0, 1, 2], target=3))  # -1
print(Solution.search(None, nums=[1], target=7))  # -1
print(Solution.search(None, nums=[1, 3], target=3))  # 1
