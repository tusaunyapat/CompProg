a = 0
count = 0
summ = a


while a!= 'q':
    a = input()
    if a == 'q':
        if count == 0:
            print('No Data')
        break
    count+=1
    summ += float(a)

if count != 0:
    print(round(summ/count,2))