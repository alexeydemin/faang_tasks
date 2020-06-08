from typing import List


class Solution:
    def reverseString(self, s) -> None:
        s = list(s)
        i = 0
        while i < len(s) / 2:
            s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
            i += 1
        print(''.join(s))
        return s


print(Solution().reverseString("Off to bed very soon"))
#print(Solution().reverseString(["h", "e", "l", "l", "o"]))  # ["o","l","l","e","h"]
#print(Solution().reverseString(["H", "a", "n", "n", "a", "h"]))  # ["h","a","n","n","a","H"]
#print(Solution().reverseString(["A"," ","m","a","n",","," ","a"," ","p","l","a","n",","," ","a"," ","c","a","n","a","l",":"," ","P","a","n","a","m","a"]))
