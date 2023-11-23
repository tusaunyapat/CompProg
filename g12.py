name = input()
num1 = ['B', 'F', 'P', 'V']
num2 = ['C', 'G','J','K','Q','S','X','Z']
num3 = ['D', 'T']
num4 = ['L']
num5 = ['M', 'N']
num6 = ['R']
num0 = ['A','E','I,','O','U','H','W','Y']

named = ''
for i in range(len(name)):
    if name[i] not in ['H', 'W']:
        named += name[i]
answer = name[0]

for i in range(len(named)):
    if named[i] in num1:
        if answer[-1]!='1' :
                answer += '1'
    if named[i] in num2:
        if answer[-1]!='2':
                answer += '2'
    if named[i] in num3:
        if answer[-1]!='3':
                answer += '3'
    if named[i] in num4:
        if answer[-1]!='4':
                answer += '4'
    if named[i] in num5:
        if answer[-1]!='5':
                answer += '5'
    if named[i] in num6:
        if answer[-1]!='6':
                answer += '6'
    if named[i] in num0:
        if answer[-1]!='-':
                answer += '-'
    
   
if len(answer) < 4:
    answer += '0'

# print(named)
# print(answer)
count = 0
ans = ''
for i in range(len(answer)):
    if answer[i]!='-':
            ans += answer[i]
            count += 1
    
    if count == 4:
        break

if len(ans) < 4:
      ans += '0'

print(ans)
