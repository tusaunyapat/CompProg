n = int(input())
data = []
for i in range(n):
    a = input()
    data.append(a)

for i in input().split():
    data.append(i)

answer = [] 

a = input()
while a != '-1':
    data.append(a)
    a = input()
answer.append(int(data[0]))

for i in range(len(data)):
    if i%2 == 0:
        answer.insert(-1,int(data[i]))
    else :
        answer.insert(0,int(data[i]))

print(answer[0:-1])