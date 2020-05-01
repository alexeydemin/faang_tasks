# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them seperately.
#
# Example
# Input: arr = [1, 2, 3]
# Output: 2
#
# Example
# Input: arr = [1, 1, 3, 3, 5, 5, 7, 7]
# Output: 0
#
# Example
# Input: arr = [1, 3, 2, 3, 5, 0]
# Output: 3
#
# Example
# Input: arr = [1, 1, 2, 2]
# Output: 2
#
# Constraints:
#
# 1 <= arr.length <= 1000
# 0 <= arr[i] <= 1000

from typing import List


class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        dic = {}
        arr.sort(reverse=True)
        for a in arr:
            if a + 1 in dic:
                count += 1
            if a not in dic:
                dic[a] = 1
        return count


#r = Solution.countElements(None, [1, 2, 3]) #2
#r = Solution.countElements(None, [1, 1, 3, 3, 5, 5, 7, 7]) #0
#r = Solution.countElements(None, [1, 3, 2, 3, 5, 0]) #3
#r = Solution.countElements(None, [1, 1, 2, 2]) #2
#r = Solution.countElements(None, [1, 1, 2, ]) #2
print(r)
