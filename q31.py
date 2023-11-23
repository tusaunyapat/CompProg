n = int(input())
teams = {}
for i in range(n):
    t, c = input().split()
    teams[t] = c
search = input().split()
while search[0] !='q':
    check = []
    is_ok = True
    for i in search:
        if i not in teams:
            print('Not OK')
            is_ok = False
            break
        if teams[i] in check:
            print('Not OK')
            print(i)
            is_ok = False
            break
        else:
            check.append(teams[i])
    if is_ok:
        print('OK')
    search = input().split()
    

# print(teams)