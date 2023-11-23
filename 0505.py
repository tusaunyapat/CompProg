data = []
answer = []
[data.append(int(i)) for i in input().split()]

data.sort()
count = 0
# print('data = ',data)

for i in range(0,len(data)):
    if data[i]!=data[i-1]:
        count+=1
        answer.append(data[i])

answer.sort()
print(count)

print(answer[:10]) if len(answer)>=10 else print(answer)
