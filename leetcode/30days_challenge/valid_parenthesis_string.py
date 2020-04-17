class Solution:
    def isValid(self, str):
        mi = ma = 0
        for s in str:
            if s == '(':
                mi += 1
                ma += 1
            elif s == ')':
                mi -= 1
                ma -= 1
            else:
                mi -= 1
                ma += 1
            if ma < 0:
                break
            mi = max(0, mi)
        return mi == 0


g = Solution.isValid(None, ')(')
print(g)
