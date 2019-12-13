class Solution:
    def reverse(self, x):
        otr = False
        if x < 0:
            otr = True
            x = -1 * x
        res = 0
        while x > 0:
            big = x
            x = x // 10
            digit = abs(big - x * 10)
            res = res * 10 + digit
        if otr:
            res = -1 * res
        if res < - pow(2, 31) or res > pow(2, 31)-1:
            return 0
        return res


a = Solution.reverse(None, -12345677)
print('===')
print(a)

# res = 0
# while x > 0:
#     big = x
#     x = x // 10
#     digit = big - x * 10
#     res = res * 10 + digit
