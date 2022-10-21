s = "abasdldfbfldkbbbaaaaaaaa"


def func(str):
    d = dict()
    mx = 0
    mr = str[0]
    for s in str:
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
        if mx < d[s]:
            mx = d[s]
            mr = s
    return mr

print(func(s))
