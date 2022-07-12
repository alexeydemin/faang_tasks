import fileinput
from collections import defaultdict


def run():
    commands = []
    # dict of variables, e.g {a:2, b:1, c:3, d:3}
    vars = {}
    # dict of number of entries, e.g. {2:1, 1:1, 3:2}
    cnt = defaultdict(lambda: 0)
    for line in fileinput.input():
        commands.append(line.strip())
    for cm in commands:
        args = cm.split()
        operator = args[0]
        if operator == 'SET':
            if args[1] in vars:
                cnt[vars[args[1]]] -= 1
            vars[args[1]] = args[2]
            cnt[args[2]] += 1
        elif operator == 'GET':
            print(vars[args[1]])
        elif operator == 'UNSET':
            cnt[vars[args[1]]] -= 1
            vars[args[1]] = 'NULL'
        elif operator == 'NUMWITHVALUE':
            print(cnt[args[1]])

run()
