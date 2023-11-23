n = int(input())
listGroup = []
group = {}

for i in range(n):
    s = input()
    listGroup.append(s)
    group[s] = []


n = int(input())
for i in range(n):
    name, g = input().split()
    group[g].append(name)


n = int(input())
answer = {}
for i in range(n):
    name, ans = input().split()
    answer[name] = ans


for key in listGroup:
    print(key)

    y = 0
    n = 0
    x = 0
    for i in group[key]:
        if i in answer:
            if answer[i] == 'Y':y += 1
            if answer[i] == 'N':n += 1
            if answer[i] == 'X':x += 1
    # print(y,n,x)

    final = ''
    if y>n and y>x:final = 'Y'
    if n>y and n>x:final = 'N'
    if x>y and x>n:final = 'X'
    if (y == n or n == x or y == x) and final =='':
        print('Inconclusive')
    else:
        w = []
        for i in group[key]:
            
            if i in answer:
                if answer[i] != final:
                    w.append(i)
        w.sort()
        if len(w) == 0:
            print('No cobra')
        else:
            print(', '.join(w))