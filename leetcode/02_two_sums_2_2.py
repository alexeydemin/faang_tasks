class Solution:
    def twoSum(self, nums, target):
        ndict = dict([(value, key) for key, value in enumerate(nums)])
        for i, a in enumerate(nums):
            if(target-a in ndict):
                return (i, ndict[target-a])


a = Solution.twoSum(None, [2, 3, 5, 6, 11, 15, 17], 16)
# a = Solution.twoSum(None, [2, 7, 11, 15], 9)
print(a)