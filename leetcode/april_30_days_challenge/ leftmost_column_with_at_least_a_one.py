# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, bm: 'BinaryMatrix') -> int:
        mn = float('inf')
        for line in binaryMatrix:
            pos = self.find_first_position(line, 0, len(line) - 1)
            if pos == 0:
                return 0
            if pos > 0:
                mn = min(pos, mn)
        if mn == float('inf'):
            mn = -1
        return mn

    def find_first_position(self, line, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        if line[middle] == 0:
            return self.find_first_position(line, middle + 1, end)
        if middle == 0:
            if line[middle] == 0:
                return -1
            else:
                return 0
        else:
            if line[middle - 1] == 1:
                return self.find_first_position(line, start, middle - 1)
            else:
                return middle


s = Solution()
print(s.leftMostColumnWithOne([[0, 0], [1, 1]]))  # 0
print(s.leftMostColumnWithOne([[0, 0], [0, 1]]))  # 1
print(s.leftMostColumnWithOne([[0, 0], [0, 0]]))  # -1
print(s.leftMostColumnWithOne([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]))  # 1
#  0 1 2 3 4 5 6 7 8 9 1 1 2 3 4 15
str = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
str = []
# 0123456789

# r = s.find_first_position(str, 0, len(str)-1) #9



# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, bm: 'BinaryMatrix') -> int:

        rows, cols = bm.dimensions()
        mn = float('inf')
        for j in range(rows):
            pos = self.find_first_position(j, bm, 0, cols-1)
            if pos == 0:
                return 0
            if pos > 0:
                mn = min(pos, mn)
        if mn == float('inf'):
            mn = -1
        return mn

    def find_first_position(self, j, bm, start, end):
        if start > end:
            return -1
        middle = (start + end) // 2
        this = bm.get(j,middle)
        if this == 0:
            return self.find_first_position(j, bm, middle + 1, end)
        if middle == 0:
            if this == 0:
                return -1
            else:
                return 0
        else:
            if bm.get(j,middle-1) == 1:
                return self.find_first_position(j, bm, start, middle - 1)
            else:
                return middle