def countMeetings(arrival, departure):
    _min = min(arrival)
    _max = max(departure)
    per = []
    r = 0
    for k, a in enumerate(arrival):
        per.append((arrival[k], departure[k]))
    for i in range(_min, _max+1):
        for j, t in enumerate(per):
            if t[0] <= i <= t[1]:
                r+=1
                del(per[j])
                break
    return r







arrival = [1, 10, 11]
departure = [11,10,11]

res = countMeetings(arrival,departure)
print(res)

