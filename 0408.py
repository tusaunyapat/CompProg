num = int(input())

for i in range(num-1):
    print('.'*(num-1-i),end='')
    print('*',end='')
    if i==0:
        print("",end='\n')
    else :
        print('.'*(i*2-1),end='')
        print('*')
print('*'*(num*2-1))