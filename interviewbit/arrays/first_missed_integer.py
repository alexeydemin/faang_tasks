class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        i = 0
        k = 0
        while k < len(A):
        #if 0 < A[i] < len(A):
            tmp = A[A[i]]
            A[A[i]] = 1
            i = tmp
            k += 1
        print(A)


# r = Solution.firstMissingPositive(None, [1, 2, 0])
# r = Solution.firstMissingPositive(None, [3, 4, 5, 1, 2, -9, 7, 8, 10, 11, -1, 0, -100])
r = Solution.firstMissingPositive(None, [1, 6, 7, 2, 4, 6, 3])
# r = Solution.firstMissingPositive(None, [-8, -7,-6])
#print(r)
