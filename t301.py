a = input()
answer = []
while a != 'q':
    a = a.split()
    # print(a[1])
    if a[1] == '+':
        answer.append(float(a[0])+float(a[2]))
    if a[1] == '-':
        answer.append(float(a[0])-float(a[2]))
    if a[1] == '*':
        answer.append(float(a[0])*float(a[2]))
    if a[1] == '/':
        answer.append(float(a[0])/float(a[2]))
    a = input()

[print(i) for i in answer]