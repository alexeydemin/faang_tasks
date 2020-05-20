from typing import List


class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        def go(hat_id, mask):
            if hat_id == 9:
                return int(mask == (1 << len(hats)) - 1)

            cnt = 0
            for person_id in range(len(hats)):
                if hat_id in hats[person_id] and (mask & (1 << person_id)) == 0:
                    cnt += go(hat_id + 1, mask | (1 << person_id))

            return cnt + go(hat_id + 1, mask)

        return go(0, 0)


print(Solution.numberWays(None, [[3, 4, 5], [3, 4, 5], [3,4, 5]]))
