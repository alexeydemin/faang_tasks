class Solution:
    def moveZeroes(self, nums):
        i = 0
        zc = 0
        while i < len(nums):
            if not nums[i]:
                nums.pop(i)
                zc+=1
            else:
                i += 1
        for i in range(zc):
            nums.append(0)
        return nums


r = Solution.moveZeroes(None, [0, 0, 1, 0, 3, 0, 12, 0])
print(r)
