from typing import List


class Solution:
    def __init__(self):
        self.res = 0

    def change(self, amount: int, coins: List[int]) -> int:
        def go(a, co):
            for i in range(len(co)):
                na = a - co[i]
                if na == 0:
                    self.res += 1
                    return 1
                if na > 0:
                    go(na, co[i:])

        go(amount, coins)

        return self.res


print(Solution().change(amount=7, coins=[1, 2, 3, 5]))  # 10
print(Solution().change(amount=5, coins=[1, 2, 5]))  # 4
print(Solution().change(amount=3, coins=[2]))  # 0
print(Solution().change(amount=10, coins=[10]))  # 1
