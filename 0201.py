# python id.py

data = list(input())
tmp = 0
for i in range(12):
    tmp += (13-i) * int(data[i])

n12 = (11 - (tmp%11))%10

for i in range(12):
    print(data[i],end='')
    if i == 0 or i == 4 or i == 9 or i == 11:
        print(' ',end='')
print(n12,end='')