from functools import cmp_to_key


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        S = []
        for a in A:
            S.append(str(a))
        S.sort(key=cmp_to_key(l_cmp))
        st = ''.join(S).lstrip('0')
        return '0' if len(st) == 0 else st


def l_cmp(a, b):
    if int(a+b) > int(b+a): return -1
    if int(a+b) < int(b+a): return 1
    if int(a+b) == int(b+a): return 0


# r = Solution.largestNumber(None, [3, 30, 34, 5, 9])
# r = Solution.largestNumber(None, [12,121])
r = Solution.largestNumber(None, [122, 12])
print(r)
