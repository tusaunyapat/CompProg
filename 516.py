n = int(input())
answer = []
answer.append(str(n))
while n != 1:
    if n%2 == 0:
        n //=2
        answer.append(str(n))
    else :
        n = 3*n +1
        answer.append(str(n))

if len(answer)>10:
    answer = answer[-15::]

answer = '->'.join(answer)
print(answer)