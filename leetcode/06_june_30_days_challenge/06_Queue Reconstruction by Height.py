from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ans = [0] * len(people)
        people.sort(key=lambda person: person[0])
        print(people)
        for el in people:
            ans[self.getIndex(ans, el[1] + 1, el[0])] = el

        return ans

    def getIndex(self, ans, k, val):
        cnt = 0
        for i, v in enumerate(ans):
            if v == 0 or v[0] == val:
                cnt += 1
            if cnt == k:
                return i


# 0 0 0 [] 0 0 0
# 1 2 3 4  5 6 7

# [[4, 4], [5, 0], [5, 2], [6, 1], [7, 0], [7, 1]]

print(Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
# print(Solution().getKthZeroIndex([0, 0, 0, 1, 0], 4))
