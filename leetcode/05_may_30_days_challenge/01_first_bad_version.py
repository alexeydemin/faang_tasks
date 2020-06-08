# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return version >= 10


class Solution:
    def __init__(self):
        self.res  = None
    def firstBadVersion(self, n):
        self.check(0, n)
        return self.res

    def check(self, start, end):
        if start <= end:
            n = (start + end) // 2
            if not isBadVersion(n-1) and isBadVersion(n):
                self.res = n
            if isBadVersion(n):
                self.check(0, n-1)
            else:
                self.check(n+1, end)
s = Solution()
print(s.firstBadVersion(10))