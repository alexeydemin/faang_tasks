# Write an algorithm to determine if a number is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

class Solution:

    def __init__(self):
        self.arr = []
        self.res = 0

    def getSum(self, n):
        s = 0
        for char in str(n):
            s += int(char) ** 2
        return s

    def getResult(self, r):
        self.res = self.getSum(r)
        if self.res != 1 and self.res not in self.arr:
            self.arr.append(r)
            self.getResult(self.res)

    def isHappy(self, n):
        self.getResult(n)
        return self.res == 1


sol = Solution()
r = sol.isHappy(23)
print(r)
