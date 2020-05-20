class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = [S[0]]
        for i in range(1, len(S)):
            if len(stack) and stack[len(stack)-1]  == S[i]:
                stack.pop()
            else:
                stack.append(S[i])
        return ''.join(stack)


print(Solution.removeDuplicates(None, 'abbaca'))
