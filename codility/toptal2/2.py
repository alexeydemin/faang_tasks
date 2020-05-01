

def solution(A):
    from collections import defaultdict
    hm = defaultdict(lambda: 0)

    k = len(set(A))
    n = len(A)
    arr = A
    l, r = 0, n

    i = 0
    j = -1
    while i < n:
        while j < n:
            j += 1

            if len(hm) < k and j < n:
                hm[arr[j]] += 1

            if len(hm) == k and ((r - l) >= (j - i)):
                l, r = i, j
                break

        if len(hm) < k:
            break

        while len(hm) == k:

            if hm[arr[i]] == 1:
                del (hm[arr[i]])
            else:
                hm[arr[i]] -= 1

            i += 1

            if len(hm) == k and (r - l) >= (j - i):
                l, r = i, j

        if hm[arr[i]] == 1:
            del (hm[arr[i]])
        else:
            hm[arr[i]] -= 1

        i += 1

    return (r - l + 1)
