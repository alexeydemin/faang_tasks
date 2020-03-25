def odd_occurency(A):
    dic = {}
    for a in A:
#        print(dic)
        if a in dic:
            del(dic[a])
        else:
            dic[a] = 1
    return list(dic.keys())[0]

#r = odd_occurency([3, 7, 9, 11, 3, 9, 11])
r = odd_occurency([3, 7, 7, 3, 7])
print(r)
