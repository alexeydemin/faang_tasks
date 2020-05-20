from typing import List


class Solution:
    def __init__(self):
        self.image = []
        self.width = 0
        self.height = 0

    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.image = image
        self.width = len(image[0])
        self.height = len(image)
        self.change_around(sr, sc, newColor)
        a = 1
        return self.image

    def change_around(self, sr, sc, nc):
        tmp = self.image[sr][sc]
        self.image[sr][sc] = nc
        if sc - 1 >= 0 and self.image[sr][sc - 1] == tmp != nc:
            self.change_around(sr, sc - 1, nc)

        if sr + 1 < self.height and self.image[sr + 1][sc] == tmp != nc:
            self.change_around(sr + 1, sc, nc)

        if sc + 1 < self.width and self.image[sr][sc + 1] == tmp != nc:
            self.change_around(sr, sc + 1, nc)

        if sr - 1 >= 0 and self.image[sr - 1][sc] == tmp != nc:
            self.change_around(sr - 1, sc, nc)


s = Solution()
r = s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
print(r)
