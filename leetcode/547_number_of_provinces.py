from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nums = isConnected
        cnt = 0

        def dfs(nums, i, j):
            if nums[i][j] != 1:
                return
            nums[i][j] = 8
            for k in range(len(nums)):
#                dfs(nums, j, k)
                dfs(nums, k, i)

        ln = len(nums)
        for i in range(ln):
            for j in range(i, ln):
                # print(i, j)
                if nums[i][j] == 1:
                    dfs(nums, i, j)
                    cnt += 1
        return cnt


isConnected = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
# 0->1, 2: 2
print(Solution.findCircleNum(None, isConnected))


isConnected = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
# 0, 1, 2: 3
print(Solution.findCircleNum(None, isConnected))


isConnected = [
    [1, 1, 0],
    [1, 1, 1],
    [0, 1, 1]
]
# 0->1->2: 1
print(Solution.findCircleNum(None, isConnected))


isConnected = [
    # 0, 1, 2, 3
    [1, 0, 1, 0],  # 0
    [0, 1, 1, 1],  # 1
    [1, 1, 1, 0],  # 2
    [0, 1, 0, 1],  # 3
]
# 0->2->1->3: 1
print(Solution.findCircleNum(None, isConnected))


isConnected = [
    # 0, 1, 2, 3
    [1, 0, 1, 0],  # 0
    [0, 1, 0, 1],  # 1
    [1, 0, 1, 0],  # 2
    [0, 1, 0, 1],  # 3
]
# 0->2, 1->3: 2
print(Solution.findCircleNum(None, isConnected))
