num = int(input())

if num<1000:
    print(num)

# K
elif num<1000000:
    if num<10000 :
        print(round(num/1000,1),end='')
    else :
        print(int(round(num/1000,0)),end='')
    print('K')

# M
elif num<1000000000:
    if num<10000000 :
        print(round(num/1000000,1),end='')
    else :
        print(int(round(num/1000000,0)),end='')
    print('M')

# B
else :
    if num<10000000000 :
        print(round(num/1000000000,1),end='')
    else : 
        print(int(round(num/1000000000,0)),end='')
    print('B')