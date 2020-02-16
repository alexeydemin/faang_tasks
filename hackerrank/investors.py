def countMeetings(arrival, departure):
    a = sorted(arrival)
    d = sorted(departure)
    _min = a[0]
    _max = d[-1]
    r = 0
    for i in range(_min, _max+1):
        for j, t in enumerate(a):
            if a[j] <= i <= d[j]:
                r+=1
                del a[j], d[j]
                break
    return r







arrival = [1, 10, 11]
departure = [11,10,11]

res = countMeetings(arrival,departure)
print(res)

