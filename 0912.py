n = int(input())
uni = set()
inter=set()
if n != 0:
    data = input().strip().split()
    uni = set(data)
    inter = set(data)
    for i in range(n-1):
        data = input().strip().split()
        data = set(data)
        uni = uni | data
        inter = inter & data
print(len(uni))
print(len(inter))
