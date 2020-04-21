def numberOfpeople(A, B):
    people = {}

    # We create a dictionary as follows:
    # {
    # 'Anne': ['Barbara'],
    # 'Barbara': ['Anne', 'Ivan'],
    # 'Ivan': ['Barbara'],
    # 'Vinny': ['Vlad'],
    # 'Vlad': ['Vinny']
    # }
    for pair in A:
        first, second = pair.split(':')

        if first not in people:
            people[first] = []
        people[first].append(second)

        if second not in people:
            people[second] = []
        people[second].append(first)

    res = []
    # For every person in our B we fill theset with friends and buddies (friends of friends) and exclude himself (-1).
    for person in B:
        theset = set()
        for friend in people[person]:
            theset.add(friend)
            for buddy in people[friend]:
                theset.add(buddy)
        res.append(len(theset) - 1)
    return res


#r = numberOfpeople(['Anne:Barbara', 'Barbara:Ivan', 'Vinny:Vlad'], ['Anne', 'Vinny'])
r = numberOfpeople(['Anne:Barbara', 'Barbara:Ivan', 'Vinny:Vlad'], ['Anne', 'Vinny'])
print(r)
