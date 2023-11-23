n = int(input())

data = {}

for i in range(n):
    name,lastname, tel = input().split()
    data[str(name+' '+lastname)] = tel
    data[tel] = str(name+' ' +lastname)

m = int(input())
for i in range(m):
    find = input()
    if find in data:
        print(find,'-->',data[find])
    else :
        print(find,'-->','Not found')