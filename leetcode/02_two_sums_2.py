class Solution:
    def twoSum(self, nums, target):
        ndict = {}
        for i, a in enumerate(nums):
            if(target-a in ndict):
                return (ndict[target-a]+1, i+1)
            else:
                ndict[a] = i


        # for i, a in enumerate(nums):
        #     for (j, b) in enumerate(nums[i+1:]):
        #         #print(i, j+i+1)
        #         if a + b == target:
        #             #print('------')
        #             return i, j+i+1

a = Solution.twoSum(None, [2, 3, 5, 6, 11, 15, 17], 16)
# a = Solution.twoSum(None, [2, 7, 11, 15], 9)
print(a)