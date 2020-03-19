class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(A)
        k = len(str(C))
        # if n < B:

        if k < B:
            return 0
        if k > B:
            if A[0] == 0 and B > 1:
                return pow(n, B) - n
            else:
                return pow(n, B)
        if k == B:
            num = 0
            for j, c in enumerate(list(str(C))):
                c = int(c)
                for i, a in enumerate(A):
                    if a < c:
                        if j + 1 != k and 0 < a:
                            num += pow(n, k - j - 1)
                        if j + 1 == k:
                            num += 1
                    elif a == c:
                        num += 1
                    else:
                        return num
            return int(num)


# r = Solution.solve(None, [2, 9], 5, 17005)
r = Solution.solve(None, [0, 1, 2, 5], 2, 21)
print(r)
