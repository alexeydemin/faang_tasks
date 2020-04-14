def compress(chars):
    anchor = write = 0
    st = ''
    for read, c in enumerate(chars):
        if read + 1 == len(chars) or chars[read + 1] != c:
            chars[write] = chars[anchor]
            write += 1
            st+=chars[anchor]
            if read > anchor:
                for digit in str(read - anchor + 1):
                    chars[write] = digit
                    write += 1
                    st += digit
            anchor = read + 1
    return write

def solution(S, K):
    arr = list(S)
    min = compress(arr)
    for i in range(len(arr)):
        ln = compress(arr[:i] + arr[K + i:])
        #print(ln)
        min = ln if min > ln else min
    return min


#print(compress()) #A3B4C

#print(solution('AABBBCCDDCCC', 3))
#print(solution('trigonome', 3))
print(solution('AABCDEEFGGGG', 4))
print(solution('AAAAABBBAAAAACD', 3))
print(solution('AAAAABCDEEEEEEEFGKKKKK', 3))
print(solution('AABCDEEFGGGG', 4))
print(solution('AABCDEEFGGGG', 4))
print(solution('AAAAAAAAAABCDE', 4))
