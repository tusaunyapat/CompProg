n = int(input())
answer = []
answer.append(n)
while n!=1:
    if n%2==0:
        n = n//2
        answer.append(n)
    else :
        n = 3*n + 1
        answer.append(n)

# print(answer)
if len(answer)>=15:
    for i in range(15):
        print(answer[len(answer)-15+i],end='')
        if i!=14:
            print('->',end='')
else :
    for i in range(len(answer)):
        print(answer[i],end='')
        if i !=len(answer)-1:
            print('->',end='')
