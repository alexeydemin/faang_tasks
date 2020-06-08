# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]):  # -> List[List[str]]:
        dic = {}
        for s in strs:
            key = ''.join(sorted(list(s)))
            if key in dic:
                dic[key].append(s)
            else:
                dic[key] = [s]

        return dic.values()


r = Solution.groupAnagrams(None, ["eat", "tea", "tan", "ate", "nat", "bat"])
print(r)
