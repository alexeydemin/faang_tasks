def max_sa(nums):
    if len(nums) == 1:
        return nums[0]
    max = float('-inf')
    current = nums[0]
    for i in range(len(nums)):
        if current < 0:
            if current > max:
                max = current
            current = nums[i]
            if current > max:
                max = current
                continue
        current += nums[i]
        if current > max:
            max = current
    return max

print(max_sa([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
