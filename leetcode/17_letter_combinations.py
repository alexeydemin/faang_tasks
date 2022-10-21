from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = {
            1: '',
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz',
        }

        def bt(i, path):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            possible_letters = letters[int(digits[i])]
            for letter in possible_letters:
                path.append(letter)
                bt(i + 1, path)
                path.pop()

        combinations = []
        bt(0, [])
        return combinations


print(Solution.letterCombinations(None, "23"))
# ["ad","ae","af","bd","be","bf","cd","ce","cf"]
