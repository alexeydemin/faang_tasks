def bioHazard(self, n, allergic, poisonous):
    rules1 = get_rules(None, allergic, poisonous)
    rules2 = get_rules(None, poisonous, allergic)
    count = 0
    a = []
    for i in range(1, n + 1):
        #print('=== step' + str(i) + '===')
        temp = []
        for elem in a:
            if is_compatible(None, elem, i, rules1):
                if is_compatible(None, elem, i, rules2):
                    temp.append(elem + [i])
                    count += 1
        a = temp
        a.append([i])
        count += 1
        print(a)
        #print('=== end step' + str(i) + '===')
    return count


def is_compatible(self, elem, i, rules):
    if i not in rules:
        return True
    for al in rules[i]:
        if al in elem:
            return False
    return True


def get_rules(self, allergic, poisonous):
    res = {}
    for i, p in enumerate(poisonous):
        if p in res:
            res[p].append(allergic[i])
        else:
            res[p] = [allergic[i]]
    return res


res = bioHazard(None, 5, [2], [2])
print(res)
#res = bioHazard(None, 4, [1, 2], [3, 4])
#print(res)

#res = bioHazard(None, 5, [1, 2], [3, 5])

#print(res)
