class Solution:

    def result_bad(self, A):
        for i, a in enumerate(A):
            print(i, a)
            if i < 2:
                continue
            if A[i] <= A[i - 2] and len(A) != i + 1:
                return i + 1
        return -1

    def turtle2(self, A):
        for i, val in enumerate(A):
            if i < 3:
                continue
                # if A[4] <= A[2] and (A[5] >= A[3] or A[0] + A[4] >= A[2] and A[1] + A[5] >= A[3] and A[3] >= A[1]):

            left_more_than_right = A[i - 1] <= A[i - 3]
            crosser_more_than_down = A[i] >= A[i - 2]
            sum_of_verticals_more_than_left = A[i - 5] + A[i - 1] >= A[i - 3]
            sum_of_horizontals_more_than_down = A[i - 4] + A[i] >= A[i - 2]
            up_more_than_down = A[i - 2] >= A[i - 4]

            if left_more_than_right and (
                    crosser_more_than_down or sum_of_verticals_more_than_left and sum_of_horizontals_more_than_down and up_more_than_down):
                return i  # + 1
        return -1

    def turtle(self, A):
        for i, val in enumerate(A):
            if i < 3:
                continue
            # case 1: 0>=2 and 3>=1
            # case 2  2=>4 and 3>=1 and 0+4>=2 and 1+5=>3
            # case 3  1=3 and 0+4 >=2
            case1 = A[i - 3] >= A[i - 1] and A[i] >= A[i - 2]
            case2 = i >= 5 and A[i - 3] >= A[i - 1] and A[i - 2] >= A[i - 4] and A[i - 5] + A[i - 1] >= A[i - 3] and A[i - 4] + A[i] >= A[i - 2]
            case3 = i >= 4 and A[i - 3] == A[i - 1] and A[i - 4] + A[i] >= A[i - 2]

            if case1 or case2 or case3:
                return i
        return -1


B = [
   [1, 3, 2, 5, 4, 4, 6, 3, 2],  # -> 6
   [4, 4, 5, 7, 8, 6, 5],  # -> 6
   [1, 1, 2, 1, 1],  # -> 4
   [1, 1, 2, 2, 4, 2, 1, 1, 2, 5, 10],  # -> 8
   [1, 1, 1, 1],  # -> 3
   [1, 1, 5, 3, 3, 2, 2, 1, 1, 3],  # -> 9
   [1, 2, 2, 1, 1]  # -> -1
]

# r = Solution.result(None, [1, 3, 2, 5, 4, 4, 6, 3, 2])
# r = Solution.result(None, [1, 1, 1, 2, 5, 4, 6, 3, 2])
# r = Solution.result(None, [1, 2, 1, 1, 2, 4, 6, 3, 2])
# r = Solution.result(None, [1, 1, 2, 2, 3, 3, 4, 4, 5, 1])
for b in B:
    r = Solution.turtle(None, b)
    print(r)
