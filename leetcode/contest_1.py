class Solution:
    def getNoZeroIntegers(self, n):
        i = 1
        while i < n:
            if '0' in str(i) or '0' in str(n - i):
                i += 1
            else:
                return [i, n - i]


a = Solution.getNoZeroIntegers(None, 11)
print(a)
