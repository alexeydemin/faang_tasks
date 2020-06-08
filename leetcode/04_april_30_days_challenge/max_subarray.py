class Solution:
    def maxSubArray(self, nums):
        max_so_far = float('-inf')
        sum = 0

        for i in range(len(nums)):
            sum += nums[i]
            if max_so_far < sum:
                max_so_far = sum

            if sum < 0:
                sum = 0
            print(sum, max_so_far)
        return max_so_far

    def cs(self, numbers: [int]) -> int:
        curSum = 0
        maxSum = float('-inf')
        for number in numbers:
            curSum += number
            maxSum = max(curSum, maxSum)
            curSum = max(curSum, 0)
            a=1
        return maxSum

#print(Solution.maxSubArray(None, [-2,-1,-3,-4,-1,-2,-1,-5,-4]))
print(Solution.cs(None,  [-2,1,-3,4,-1,2,1,-5,4]))