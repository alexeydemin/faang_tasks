class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        C = sorted(A + B)
        l = len(C)
        if l%2:
            return C[l//2]
        else:
            print(C, l // 2, l//2-1, C[l // 2], C[l // 2-1], C[l//2] + C[l//2-1], (C[l//2] + C[l//2-1])/2)
            return (C[l//2] + C[l//2-1])/2


#r = Solution.findMedianSortedArrays(None, [1, 4, 5], [2, 3])
#r = Solution.findMedianSortedArrays(None, [1], [ 3])
r = Solution.findMedianSortedArrays(None, [0,23], [])
#print(r)
