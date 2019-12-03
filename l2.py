def answer(s):
    lst_l = []
    lst_r = []
    for k, ch in enumerate(s):
        if ch == '>':
            lst_r.append(k)
        if ch == '<':
            lst_l.append(k)
    cnt = 0
    for l in lst_l:
        for r in lst_r:
            if r < l:
                cnt += 1

    return cnt*2


print answer('--->-><-><-->-')
print answer(">----<")
print answer("<<>><")
