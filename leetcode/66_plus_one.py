from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Take last element and add 1
        # if result > 9 (== if current element is 9):
        # take next element and increase it to one, current put to 0
        n = len(digits) - 1
        digits = Solution.inc(digits, n)
        return digits

    def inc(d, n):
        if n == -1:
            d.insert(0, 1)
            return d
        if d[n] == 9:
            d[n] = 0
            return Solution.inc(d, n - 1)
        else:
            d[n] += 1
        return d


print(Solution.plusOne(None, [1, 2, 3]))  # 124
print(Solution.plusOne(None, [4, 3, 2, 1]))  # 4322
print(Solution.plusOne(None, [4, 3, 2, 9]))  # 4330
print(Solution.plusOne(None, [9]))  # 10
