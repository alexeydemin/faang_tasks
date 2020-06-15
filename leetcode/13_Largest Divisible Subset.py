from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        d = {}
        for num in sorted(nums):
            d[num] = [num]
            for key in sorted(d, key=lambda k: len(d[k]), reverse=True):
                if num != key and not num % key:
                    d[num] = d[key] + d[num]
                    break
        max_key = max(d, key=lambda x: len(set(d[x])))
        return d[max_key]


# print(Solution().largestDivisibleSubset([]))
print(Solution().largestDivisibleSubset([4, 8, 10, 240]))  # 4,8,240
# print(Solution().largestDivisibleSubset([1, 2, 3, 4, 7, 9, 35, 70, 105, 140, 210, 420]))
