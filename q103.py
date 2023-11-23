# calculator only + - (input -> string)
problem = input()
number = []
operator = []

for i in range(len(problem)):
    if problem[i] == '-' or problem[i] == '+':
        operator.append(problem[i])
a = ''
for i in range(len(problem)):
    if (problem[i] == '-' or problem[i] == '+') and i != 0 :
        a = int(a)
        number.append(a)
        a = ''    
    else :
        a += problem[i]

    if i == len(problem)-1:
        a = int(a)
        number.append(a)


if problem[0] == '-':
    operator.remove('-')

answer = number[0]

for i in range(len(operator)):
    a = 0
    if operator[i] == '+':
        answer += number[i+1]
    else:
        answer -= number[i+1]

print(answer)
