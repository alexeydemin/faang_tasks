class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer
    def searchMatrix(self, A, B):
        arr = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                arr.append(A[i][j])


        start = 0
        end = len(arr)-1

        while start <= end:
            mid = (start + end) // 2
            #print(start, mid, end)
            if arr[mid] == B:
                return 1
            elif arr[mid] < B:
                start = mid + 1
            else:
                end = mid - 1
        return 0



r = Solution.searchMatrix(None, [[1,2,3], [4,6, 7]], 5)
print(r)