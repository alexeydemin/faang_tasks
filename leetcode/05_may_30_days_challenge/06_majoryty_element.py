from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for c in nums:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
            if dic[c] > len(nums)/2:
                return c
r = Solution.majorityElement(None, [1])
print(r)