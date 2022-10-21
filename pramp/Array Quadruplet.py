def find_array_quadruplet(arr, s):
    if len(arr) < 4:
        return []
    arr.sort()
    arr = list(set(arr))
    # return arr
    n = len(arr)
    p1 = 0  # 0
    p2 = round(n / 3)  # 1
    p3 = round(n // 3 * 2)  # 2
    p4 = n - 1  # 4
    # print(p1, p2, p3, p4)
    while 0 <= p1 < p2 < p3 < p4 < n:
        current_s = arr[p1] + arr[p2] + arr[p3] + arr[p4]
        print(p1, p2, p3, p4, current_s)
        # print(str(arr[p1]) + '+' + str(arr[p2]) + '+' + str(arr[p3]) + '+' + str(arr[p4]) + ' = ' + str(current_s))
        if current_s == s:
            return sorted([arr[p1], arr[p2], arr[p3], arr[p4]])
        elif current_s < s:
            if p3 + 1 != p4:
                p3 += 1
            else:
                if p2 + 1 != p3:
                    p2 += 1
                    print('p2++')
                else:
                    p1 += 1
        else:
            if p4 - 1 != p3:
                p4 -= 1
            else:
                if p3 - 1 != p2:
                    p3 -= 1
                else:
                    p2 -= 1
                    print('p2--')
    return []


# print(find_array_quadruplet(arr=[2, 7, 4, 0, 9, 5, 1, 3], s=20))  # [0, 4, 7, 9]
# print(find_array_quadruplet(arr=[1, 2, 3, 4], s=20))  # []
#                            0  1  2  3  4  5  6   7   8   9
# print(find_array_quadruplet([1, 2, 3, 4, 5, 9, 19, 12, 12, 19], 40))  # [4,5,12,19]

print(find_array_quadruplet([1, 2, 3, 4, 5, 9, 12, 19], 40))  # [4,5,12,19]
1, 5, 12, 19
1, 9, 12, 19