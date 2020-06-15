class Solution:                                                                                                                                            
    def reverseParentheses(self, s: str) -> str:
        stack = ['']
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                add = stack.pop()[::-1]
                stack[-1] += add
            else:
                stack[-1] += c
        return stack.pop()







#print(Solution().reverseParentheses("(abcd)"))  # dcba
print(Solution().reverseParentheses("(u(love)i)")) #iloveu
# print(Solution().reverseParentheses("(ed(et(oc))el)")) #iloveu
# print(Solution().reverseParentheses("(ed(et(oc))el)")) #leetcode
# print(Solution().reverseParentheses("a(bcdefghijkl(mno)p)q")) #apmnolkjihgfedcbq
