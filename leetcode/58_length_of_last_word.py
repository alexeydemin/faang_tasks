class Solution:
    def lengthOfLastWord(self, s: str):
        count = 0
        for i in range(1, len(s) + 1):
            if s[-i] != ' ':
                count += 1
            else:
                if count:
                    return count
        return count


print(Solution.lengthOfLastWord(None, "Hello"))  # 5
print(Solution.lengthOfLastWord(None,    'fly me   to   the moon  ')) #4
print(Solution.lengthOfLastWord(None, "luffy is still joyboy")) #6
