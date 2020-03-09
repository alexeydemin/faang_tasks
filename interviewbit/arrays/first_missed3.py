class Solution:
    def firstMissingPositive(self, A):
        i = 0
        while i < len(A):
            # print(i, A, A[i], A[A[i] - 1], 'Y' if 0 < A[i] <= len(A) else 'N')
            if 0 < A[i] <= len(A) and A[i] != i + 1 and A[A[i] - 1] != A[i]:
                a = A[i]
                b = A[A[i] - 1]
                A[A[i] - 1], A[i] = a, b
                # A[i], A[A[i] - 1] = A[A[i] - 1], A[i]
            else:
                i += 1
        #print(A)
        i=0
        while i<len(A) and A[i] == i+1:
            i+=1
        return i+1


# A = [3, 4, -1, 1]
# A = [1, 1, 1]
A = [10, -5, 4, 3, 2, 13, -1, 0, 0, 1]
A = [10, -5, 4, 3, 2, 13, -1, 0, 0, 1]
# A = [5, 6, 8, 4, 1, 2, 3, 0, -1]
r = Solution.firstMissingPositive(None, A)
print(r)
