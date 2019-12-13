class Solution:
    def isPalindrome(self, x):
        z = x
        if x < 0:
            return False
        res = 0
        while x > 0:
            big = x
            x = x // 10
            digit = abs(big - x * 10)
            res = res * 10 + digit
        if z == res:
            return True
        return False


a = Solution.isPalindrome(None, 10001)
print('===')
print(a)

# res = 0
# while x > 0:
#     big = x
#     x = x // 10
#     digit = big - x * 10
#     res = res * 10 + digit
