from typing import List


class Solution:
    def subarraySum1(self, nums: List[int], k: int) -> int:
        l = len(nums)
        cnt = 0
        for i in range(l+1):
            for j in range(l+1):
                if j > i:
                    print ('{:d} {:d} {:10s}{:3d}'.format(i, j, str(nums[i:j]), sum(nums[i:j])) )
                    if sum(nums[i:j]) == k:
                        cnt+=1

        return cnt

    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        s = [[0 for _ in range (n)] for o in range(n)]
        for i in range(0, n):
            s[0][i] = s[0][i-1] + nums[i]
            if s[0][i] == k:
                cnt+=1
        for i in range(1, n):
            for j in range(i,n):
                s[i][j] = s[i-1][j] - nums[i-1]
                if s[i][j] == k:
                    cnt += 1
        print(s)
        return cnt


print(Solution.subarraySum(None, [1, 1, 1], 2))
#print(Solution.subarraySum(None, [7, 5, 3, 8, 1], 8))
