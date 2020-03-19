import math


class Solution:
    def arrange(self, A):
        n = len(A)
        for i in range(n):
            old = A[i]
            new = A[A[i]]
            print(old, new)
            A[i] = (new +1)
            #A[i]  = A[i]//n
        #    A[i] = temp//n
        #for i in range(n):
         #    A[i] = A[i] / n


# [6, 2, 0, 7, 5, 3, 1, 4]
# 3 4 2 0 1
A = [7, 5, 3, 0, 1, 2, 4, 6]
# A =  [ 4, 0, 2, 1, 3 ]
Solution.arrange(None, A)

print(A)
