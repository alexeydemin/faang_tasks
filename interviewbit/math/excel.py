class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        al = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        alph = {a: i + 1 for i, a in enumerate(al)}  # {A:1,B:2, ..., Z:26}
        g = 0
        for i, l in enumerate(list(A)):
            g = g * 26 + alph[l]
        return g


r = Solution.titleToNumber(None, 'ZZ')
print(r)
