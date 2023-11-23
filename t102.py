number = input()
length = len(number)

if length %3 == 0:
    for i in range(length):
        print(number[i],end='')
        if i%3 == 2 and i != length - 1:
            print(',',end='')
if length %3 == 1:
    for i in range(length):
        print(number[i],end='')
        if i%3 == 0 and i != length - 1:
            print(',',end='')
if length %3 == 2:
    for i in range(length):
        print(number[i],end='')
        if i%3 == 1 and i != length - 1:
            print(',',end='')