stations = {}

while True:
    data = input().split()
    if len(data) == 1:
        find = data[0]
        break
    else:
        if data[0] not in stations:
            stations[data[0]] = []
        if data[1] not in stations:
            stations[data[1]] = []

        stations[data[0]].append(data[1])
        stations[data[1]].append(data[0])
# print(stations)
if find not in stations:
    answer = [find]
else:
    answer = stations[find]
# print(answer)
    ans = []
    for i in answer:
        for j in stations[i]:
            if j not in answer and j not in ans :
                ans.append(j)

    answer += ans
ANS = sorted(list(set(answer)))

[print(i) for i in ANS]
