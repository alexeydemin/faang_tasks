from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0 for _ in range(len(T))]
        stack = []
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            ans[i] = abs(stack[-1] - i) if stack else 0
            stack.append(i)
        return ans


print(Solution().dailyTemperatures(T=[73, 74, 75, 71, 69, 72, 76, 73])) #[1, 1, 4, 2, 1, 1, 0, 0]
