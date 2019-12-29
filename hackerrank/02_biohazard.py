def bioHazard_old(n, allergic, poisonous):
    rules = get_rules(allergic, poisonous)
    #   print(rules)

    count = 0
    a = []
    for i in range(1, n + 1):
        # print('=== step' + str(i) + '===')
        temp = []
        for elem in a:
            if is_compatible(elem, i, rules):
                temp.append(elem + [i])
                count += 1
        a = temp
        a.append([i])
        count += 1
        print(a)
        # print('=== end step' + str(i) + '===')
    return count


def is_compatible(elem, i, rules):
    if i not in rules:
        return True
    for al in rules[i]:
        if al in elem:
            return False
    return True


def get_rules(allergic, poisonous):
    res = {}
    for i, p in enumerate(poisonous):
        if p in res:
            res[p].append(allergic[i])
        else:
            res[p] = [allergic[i]]

    for j, a in enumerate(allergic):
        if a in res:
            res[a].append(poisonous[j])
        else:
            res[a] = [poisonous[j]]
    return res


# for m in range(1, 21):
#     res = bioHazard(m, [], [])
#     print(m, res, int((m+1)*m/2))

# res = bioHazard(8, [], [])

# print(res)

#  2 3 4 5 6  7  8
# 1       5 6  7  8  8 (8-1+1)
# 2       8 10 12 14 7 (8-2+1)
# 3       9 12 15 18 6 (8-3+1)
# 4       8 12 16 20 5 (8-4+1)_
# 5       5 10 15 20 4 (8-5+1)
# 6       0 6  12 18 3
# 7       0 0  7  14 2
# 8               8

# entries = ()
def entries_num(n, digit):
    return (n - digit + 1) * digit


# r = entries_num(3, 2)
# print(r)

def bh2(m, al, po):
    pers = int((m + 1) * m / 2)
    for i, a in enumerate(al):
        big_digit = max(al[i], po[i])
        small_digit = min(al[i], po[i])
        sub = (m - big_digit + 1) * small_digit
        pers -= sub
    return pers


def bh3(m, al, po):
    f = [[0] * m for i in range(m)]
    for i in range(m):
        for j in range(m):
            if i >= j:
                f[i][j] = 1
    print(f)
    print(al)
    print('====')
    for k, a in enumerate(al):
        print(al[k], po[k])
        big = max(al[k], po[k])
        print('big =' + str(big))
        small = min(al[k], po[k])
        print('small =' + str(small))
        print('----')
        for j in range(1, small + 1):
            for i in range(big, m + 1):
                print('i=' + str(i), 'j=' + str(j))
                f[i - 1][j - 1] = 0
    print('===end===')
    print(f)
    return sum(sum(f, []))


# r = bh2(4, [1, 2], [3, 4])
# print(r)
# r = bh3(5, [1, 2], [3, 5])
# print(r)


def bioHazard4(m, al, po):
    # f = [[0] * m for i in range(m)]
    f = []
    for i in range(m):
        # print(i)
        f.append([0] * m)
        for j in range(m):
            if i >= j:
                f[i][j] = 1

    for k, a in enumerate(al):
        big = max(al[k], po[k])
        small = min(al[k], po[k])
        for j in range(0, small):
            for i in range(big - 1, m):
                f[i][j] = 0
    return sum(map(sum, f))


def bioHazard4(m, al, po):
    f = {}
    for k, a in enumerate(al):
        big = max(al[k], po[k])
        small = min(al[k], po[k])
        for j in range(0, small):
            for i in range(big - 1, m):
                f[str(i) + str(j)] = 1
    return int((m + 1) * m / 2 - len(f))


r = bioHazard4(5, [1, 2], [3, 5])
print(r)
