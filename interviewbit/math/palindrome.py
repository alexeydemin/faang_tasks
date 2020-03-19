class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        A = list(str(A))
        for i in range(round(len(A) / 2)):
            if A[i] != A[len(A)-i-1]:
                return False
        return True

r = Solution.isPalindrome(None, 12321)
print(r)
