class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        _max = 0
        S = []
        for i, a in enumerate(A):
            while S and A[S[-1]] <= a:
                pivot = S.pop()
                if S and A[pivot] < a:
                    _max = max(_max, S[-1] * i)
            S.append(i)
        return _max % 1000000007


r = Solution.maxSpecialProduct(None, [7, 14, 8, 9, 11, 5, 1, 0])
print(r)
