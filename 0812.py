n = int(input())
data = {}
find = []
for i in range(n):
    name, nickname = input().split()

    data[name] = nickname
    data[nickname] = name

m = int(input())
for i in range(m):
    n = input()
    print(data[n]) if n in data else print('Not found')

