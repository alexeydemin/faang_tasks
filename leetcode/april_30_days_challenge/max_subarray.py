class Solution:
    def maxSubArray(self, nums):
        max_so_far = float('-inf')
        max_ending_here = 0

        for i in range(len(nums)):
            max_ending_here += nums[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here

            if max_ending_here < 0:
                max_ending_here = 0
            print(max_ending_here, max_so_far)
        return max_so_far

#print(Solution.maxSubArray(None, [-2,-1,-3,-4,-1,-2,-1,-5,-4]))
print(Solution.maxSubArray(None, [-2,-1,-3,4,-1,2,1,-5,4]))