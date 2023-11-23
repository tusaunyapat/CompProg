n = int(input())
groups = {}
departments = {}
years ={}
data = {}
ans = set()
for i in range(n):
    name, group, year, department = input().split()
    ans.add(name)
    data[name] = name + ' ' + group + ' ' + year + ' ' + department
    if group not in groups:
        groups[group] = set()
    groups[group].add(name)

    if year not in years:
        years[year] = set()
    years[year].add(name)

    if department not in departments:
        departments[department] = set()
    departments[department].add(name)

search = input().split()
for i in range(len(search)):
        if search[i] in groups:
            ans = ans & groups[search[i]]
        if search[i] in departments:
            ans = ans & departments[search[i]]
        if search[i] in years:
            ans = ans & years[search[i]]

if len(ans) == n or len(ans) == 0:
    print('Not Found')
else :
    answer = sorted(ans)
    [print(data[i]) for i in answer]

