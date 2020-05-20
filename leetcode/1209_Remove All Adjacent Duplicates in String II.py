class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [s[0]]
        cnt = [1]
        for i in range(1, len(s)):
            if len(stack) and stack[len(stack) - 1] == s[i]: # equal to previous
                cnt[len(cnt)-1] += 1
                stack.append(s[i])
                if cnt[len(cnt)-1] == k:
                    stack = stack[:len(stack) - k]
                    cnt.pop()
            else: # not equal to previous
                stack.append(s[i])
                cnt.append(1)

        return ''.join(stack)


print(1, Solution.removeDuplicates(None, 'abcd', 2)) #abcd
print(2, Solution.removeDuplicates(None, 'deeedbbcccbdaa', 3))  # aa
print(3, Solution.removeDuplicates(None, 'pbbcggttciiippooaais', 2))  # ps
