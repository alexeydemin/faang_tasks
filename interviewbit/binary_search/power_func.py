class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer

    def __init__(self):
        self.y = 0

    def pow(self, x, n, d):

        self.po(x, n)  # % d
        if n % 2:
            self.y *= x
        return self.y  # %d

    def po(self, x, n):
        mid = n // 2
        if mid:
            self.y = x * x
            self.po(self.y, mid)


s = Solution()
r = s.pow(71045970,41535484,64735492)
#r = s.pow(3, 3, 64735492)
# r = s.pow(2, 3, 3)
print(r)
