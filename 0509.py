import math

num = int(input())

x = []
y = []
dis = []

for i in range(num):
    a,b = [float(i) for i in input().split()]
    x.append(a)
    y.append(b)
    dis.append(math.sqrt(a*a + b*b))

answer = list(zip(dis,x,y))
answer.sort()
answerIndex = dis.index(answer[2][0])
print(f'#{answerIndex+1}: ({answer[2][1]}, {answer[2][2]})')
    


