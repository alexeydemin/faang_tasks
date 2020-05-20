class Solution(object):
    def maxSubarraySumCircular(self, A):
        print(list(-A[i] for i in range(1, len(A))))
        print(list(-A[i] for i in range(len(A) - 1)))
        def kadane(A):
            mx = sm = 0
            for x in A:
                sm = x + max(sm, 0)
                mx = max(mx, sm)
            return mx

        S = sum(A)
        ans1 = kadane(A)
        ans2 = S + kadane(-A[i] for i in range(1, len(A)))
        ans3 = S + kadane(-A[i] for i in range(len(A) - 1))
        return max(ans1, ans2, ans3)



# [5, -3, 5, 5, -3, 5]
#  0   1  2  3  4  5


#print(Solution.maxSubarraySumCircular(None, [1, -2, 3, -2]))  # 3
print(Solution.maxSubarraySumCircular(None, [5, -3, 5]))  # 10
#print(Solution.maxSubarraySumCircular(None, [3, -1, 2, -1]))  # 4
#print(Solution.maxSubarraySumCircular(None, [3, -2, 2, -3]))  # 3
#print(Solution.maxSubarraySumCircular(None, [-2, -3, -1]))  # -1
#print(Solution.maxSubarraySumCircular(None, [2, -1, 4]))  # 6
#print(Solution.maxSubarraySumCircular(None, [-2, -1, -3, 4, -1, 2, 1, -5, 4]))  # 6
