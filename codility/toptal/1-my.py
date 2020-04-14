def compress(st):
    n = len(st)
    res = ''
    arr = []
    i = 0
    while i < n:
        cnt = 1
        while i < n - 1 and st[i] == st[i + 1]:
            cnt += 1
            i += 1
        s = (str(cnt) if cnt > 1 else '') + st[i]
        res += s
        arr.append((cnt, st[i]))
        i += 1
        #print(res)
    return (len(res), res)


def solution(S, K):
    arr = []
    #print(S)
    for i in range(len(S) - K + 1):
        #print(S[:i] + K * 'x' + S[K + i:], compress(S[:i] + S[K + i:])[0], compress(S[:i] + S[K + i:])[1])
        arr.append(compress(S[:i] + S[K + i:]))
    return min(arr)

def test(s, K, res):
    print(s, solution(s, K), solution(s, K)[0] == len(res))

test('AABCDEEFGGGG',           4, 'A2EF4G')
test('AAAAABBBAAAAACD',        3, '10ACD')
test('AAAAABCDEEEEEEEFGKKKKK', 3, '5A7EFG5K')
test('AABCDEEFGGGG', 4, 'A2EF4G')
test('AABCDEEFGGGG', 4, '2AEF4G')
test('AAAAAAAAAABCDE', 4, '10A')
test('ABCDDF', 0, 'ABC2DF')
test('ABCDDF', 1, 'ABCDF')
