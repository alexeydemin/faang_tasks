class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        print('initial=' + str(A))
        i = 0
        while i < len(A):
            print('i=' + str(i))
            if A[i] is True or( A[i] > len(A) or A[i] < 1):
                test = True
            else:
                Solution.assignTrue(None, A, A[i])
            i+=1
        for _k, el in enumerate(A):
            if el == True and type(el) == type(True):
                continue
            else:
                return _k+1

        return 'xx'

    def assignTrue(self, A, j):
        print('assignTrue(), j= ' + str(j))
        if A[j-1] is True or (A[j-1] > len(A) or A[j-1] < 1):
            A[j - 1] = True
            print('Exiting assignTrue() for some reason')
            return
        temp = A[j-1]
        A[j-1] = True
        print(A)
        Solution.assignTrue(None, A, temp)


#r = Solution.firstMissingPositive(None, [10, 5, 8, 7, 6, 3,2,1])
#r = Solution.firstMissingPositive(None, [17, 80, 1, -5, 2])
r = Solution.firstMissingPositive(None, [-1, 4, 1, 3, 2])
print(r)
