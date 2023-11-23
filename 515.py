data = [int(e) for e in input().split()]
data.sort()

number = []
check = data[0]
number.append(check)

for i in range(len(data)):
    if data[i] != check:
        number.append(data[i])
        check = data[i]
print(len(number))
if len(number)>10:
    print(number[0:10])
else:
    print(number)