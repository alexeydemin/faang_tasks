class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        l1 = sorted(list(s1))
        l2 = sorted(list(s2))
        r = 1
        s = 1
        for i in range(len(s1)):
            r *= int(l1[i] <= l2[i])
            s *= int(l1[i] >= l2[i])
        return bool(s + r)


print(Solution.checkIfCanBreak(None, 'abc', 'xya'))
print(Solution.checkIfCanBreak(None, 'abe', 'acd'))
print(Solution.checkIfCanBreak(None, 'leetcode', 'interview'))


