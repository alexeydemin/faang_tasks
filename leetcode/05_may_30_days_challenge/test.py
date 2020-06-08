from typing import List


class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ia = ib = 0
        ret = []
        while ia < len(A) and ib < len(B):
            if max(A[ia][0], B[ib][0]) <= min(A[ia][1], B[ib][1]):
                ret.append([
                    max(A[ia][0], B[ib][0]),
                    min(A[ia][1], B[ib][1]),
                ])

            if A[ia][1] < B[ib][1]:
                ia += 1
            else:
                ib += 1
        return ret


A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]
print(Solution.intervalIntersection(None, A, B) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]])
