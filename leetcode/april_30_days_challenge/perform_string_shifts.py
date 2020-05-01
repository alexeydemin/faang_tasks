from typing import List


class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for sh in shift:
            if sh[0]:  # right
                s = s[-sh[1]:] + s[:-sh[1]]
            else:  # left
                s =  s[sh[1]:] + s[:sh[1]]
        return s


print(Solution.stringShift(None, s = "abcdefg", shift = [[1,1],[1,1],[0,2],[1,3]]))
#print(Solution.stringShift(None, s="abcdefg", shift=[[1, 1]]))
#print(Solution.stringShift(None, s="abcdefg", shift=[[0, 1]]))
