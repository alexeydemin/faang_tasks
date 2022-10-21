from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = {}
        digit_logs = []

        for log in logs:
            raw = log.split(" ")
            if raw[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs[raw[0]] = log
        print(letter_logs.items())
        letter_logs = sorted(letter_logs.items(), key=lambda x: (" ".join( x[1].split(" ")[1:]), x[0]))
        letter_logs = [x[1] for x in letter_logs]

        return letter_logs + digit_logs


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
print(Solution.reorderLogFiles(None, logs))
#["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
