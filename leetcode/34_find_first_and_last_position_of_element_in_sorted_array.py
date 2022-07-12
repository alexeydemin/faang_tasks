from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bss(arr, start, end, target):
            if start > end:
                return -1
            mid = (start + end) // 2
            if (mid - 1 < 0 or arr[mid - 1] != target) and arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return bss(arr, mid + 1, end, target)
            else:
                return bss(arr, start, mid - 1, target)

        def bse(arr, start, end, target):
            # print(start, end)
            if start > end:
                return -1
            mid = (start + end) // 2
            if arr[mid] == target and (mid + 1 > len(arr) - 1 or arr[mid + 1] != target):
                return mid
            elif arr[mid] == target and mid + 1 <= len(arr) - 1 and arr[mid + 1] == target:
                return bse(arr, mid + 1, end, target)
            else:
                return bse(arr, start, mid - 1, target)

        if len(nums) == 1 and target == nums[0]:
            return [0, 0]
        start_point = bss(nums, 0, len(nums) - 1, target)
        if start_point == -1:
            return [-1, -1]
        end_point = bse(nums, start_point, len(nums) - 1, target)
        # if end_point == -1:
        #     return [start_point, len(nums) - 1]
        return [start_point, end_point]

        # res = []
        # for i, n in enumerate(nums):
        #     if n == target:
        #         res.append(i)
        # return [res[0], res[-1]] if len(res) else [-1, -1]


print(Solution.searchRange(None, nums=[0, 0, 1, 2, 2], target=0))  # [0,1]
print(Solution.searchRange(None, nums=[2, 2], target=2))  # [0,1]
print(Solution.searchRange(None, nums=[3, 3, 3], target=3))  # [0,2]
print(Solution.searchRange(None, nums=[2], target=2))  # [0,0]
print(Solution.searchRange(None, nums=[5, 7, 7, 8, 8, 10], target=8))  # [3,4]
print(Solution.searchRange(None, nums=[5, 7, 7, 8, 8, 10], target=6))  # [-1,-1]
print(Solution.searchRange(None, nums=[5, 7, 7, 8, 10], target=8))  # [3, 3]
print(Solution.searchRange(None, nums=[], target=0))  # [-1,-1]
