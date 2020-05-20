from typing import List


class Solution:
    def checkStraightLine(self, data: List[List[int]]) -> bool:
        if data[1][0] - data[0][0]:
            a = (data[1][1] - data[0][1]) // (data[1][0] - data[0][0])
        else:
            a = 0
        b = data[0][1] - data[0][0] * a

        for i in range(2, len(data)):
            if data[i][1] != a * data[i][0] + b:
                return False
        return True




#print(Solution.checkStraightLine(None, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))  # true
#print(Solution.checkStraightLine(None, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [7, 7]]))  # false
print(Solution.checkStraightLine(None, [[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]))  # false
