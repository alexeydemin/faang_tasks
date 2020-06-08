from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s = 0
        for n in nums:
            s^=n
        return s


#print(Solution.singleNonDuplicate(None, [1, 1, 2, 3, 3, 4, 4, 8, 8]))
print(Solution.singleNonDuplicate(None, [3,3,7,7,10,11,11]))
#print(Solution.singleNonDuplicate(None, [1,1,2]))
