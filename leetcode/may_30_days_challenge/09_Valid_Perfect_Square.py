class Solution:
    def __init__(self):
        self.res = False

    def run(self, sta, end, num):
        if sta > end:
            return
        a = (sta + end) // 2
        if a * a == num:
            self.res = True
        if a * a > num:
            self.run(sta, a - 1, num)
        else:
            self.run(sta + 1, end, num)

    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        if num == 4: return True
        self.run(3, num // 2, num)

        return self.res




s = Solution()
# print(s.isPerfectSquare(1))
# print(s.isPerfectSquare(2))
# print(s.isPerfectSquare(3))
# print(s.isPerfectSquare(4))
# print(s.isPerfectSquare(9))
print(s.isPerfectSquare(4))
#s = Solution()
#print(s.isPerfectSquare(17))
