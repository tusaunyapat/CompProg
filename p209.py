n = int(input())
v = list()

for i in range(n):
    raw = input().split()
    v.append(raw)

c = input().split()

if c[0] == 'show':
    for i in v:
        [print(j, end=' ') for j in i]
        print('')

if c[0] == 'get':
    check = False
    for i in range(len(v)):
        if v[i][0] == c[1]:
            [print(j, end = ' ') for j in v[i]]
            check = True
    if not check:
        print(c[1], 'not found')

if c[0] == 'avg':
    Sum = 0
    for i in range(len(v)):
        Sum += float(v[i][int(c[1])])
    print(round(Sum/len(v),4))

if c[0] == 'max':
    Max = 0
    name= ''
    v.sort()
    for i in range(len(v)):
        if float(v[i][int(c[1])]) > Max:
            Max = float(v[i][int(c[1])])
            name = v[i][0]
    print(name, Max)

if c[0] == 'sort':
    new = []
    v.sort()
    for i in range(len(v)):
        new.append([float(v[i][int(c[1])]),v[i][0]])
    new.sort()
    # print(new)
    [print(new[i][1], end=' ') for i in range(len(new))]
