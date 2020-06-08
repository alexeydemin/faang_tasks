from typing import List
from random import choices

class Solution:

    def __init__(self, w: List[int]):
        self.w = w

    def pickIndex(self) -> int:
        return choices(range(len(self.w)), self.w)[0]


obj = Solution([1, 3])
print(obj.pickIndex())
