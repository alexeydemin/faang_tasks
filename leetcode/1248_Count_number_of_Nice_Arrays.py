from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        dic = {0:1}
        res = cnt = 0
        for a in nums:
            if a & 1:
                cnt += 1
            if cnt - k in dic:
                res += dic[cnt - k]
            dic[cnt] = dic.get(cnt, 0) + 1

        return res
        # cnt = 0
        # for i in range(len(nums)):
        #     odd = 0
        #     for j in range(i, len(nums)):
        #         if nums[j] & 1:  # odd
        #             odd += 1
        #         if odd == k:
        #             cnt += 1
        # return cnt


print(Solution.numberOfSubarrays(None, nums=[1, 1, 2, 1, 1], k=3))  # 2
#print(Solution.numberOfSubarrays(None, nums=[2, 4, 6], k=1))  # 0
#print(Solution.numberOfSubarrays(None, nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2))  # 16
