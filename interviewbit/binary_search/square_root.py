import math


class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A in (1,0):
            return A
        start = 1
        end = A
        while start <= end:
            mid = (start + end) // 2

            print(start, mid, end)
            if mid * mid == A:
                return mid
            elif mid * mid < A:
                start = mid + 1
                val = mid
            else:
                end = mid - 1
        return val


r = Solution.sqrt(None, 1)
print(r)
