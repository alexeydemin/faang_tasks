class Solution:
    def twoSum(self, nums, target):
        for i, a in enumerate(nums):
            for (j, b) in enumerate(nums[i+1:]):
                #print(i, j+i+1)
                if a + b == target:
                    #print('------')
                    return i, j+i+1

a = Solution.twoSum(None, [2, 3, 5, 6, 11, 15, 17], 16)
print(a)

# def simpleArraySum(ar):
#     sum = 0
#     for a in ar:
#         sum += a
#     return sum
#
#
# print (simpleArraySum([1, 2, 3, 4, 5]))
