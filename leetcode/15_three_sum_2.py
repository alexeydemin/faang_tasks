class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        x = set()
        for i, first in enumerate(nums):
            start_i = i+1
            end_i = len(nums)-1
            while start_i < end_i:
                sum = first + nums[start_i] + nums[end_i]
                if sum < 0:
                    start_i = start_i + 1
                if sum > 0:
                    end_i = end_i - 1
                if sum == 0:
                    x.add((first, nums[start_i], nums[end_i]))
                    start_i = start_i + 1
                    end_i = end_i - 1
        ret = []
        for el in x:
            ll = list(el)
            ret.append(ll)
        return x

g = Solution.threeSum(None, [-1, 0, 1, 2, -1, -4])
print(g)
