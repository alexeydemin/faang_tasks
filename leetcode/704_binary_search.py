from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bs(arr, start, end, target):
            if start > end:
                return -1
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return bs(arr, mid + 1, end, target)
            else:
                return bs(arr, start, mid - 1, target)
        return bs(nums, 0, len(nums) - 1, target)


print(Solution.search(None, nums=[-1, 0, 3, 5, 9, 12], target=9))  # 4
print(Solution.search(None, nums=[-1, 0, 3, 5, 9, 12], target=2))  # -1
