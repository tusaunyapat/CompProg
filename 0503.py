num = int(input())
data = []
# 1
for i in range(num):
    a = int(input())
    data.append(a)
# 2
[data.append(int(i)) for i in input().split()]

# 3
a = 0
while a!=-1:
    a = int(input())
    if a!=-1:
        data.append(a)

# sort
answer = []
for i in range(len(data)):
    if i%2==0:
        answer.append(data[i])
    else :
        answer.insert(0,data[i])
# print(data)
print(answer)