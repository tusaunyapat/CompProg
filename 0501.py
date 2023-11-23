check = [False]*10

string = input()

for i in range(len(string)):
    
    if ord(string[i])>=48 and ord(string[i])<=57:
        # print('check ',string[i])
        check[int(string[i])] = True

count = 0
for i in range(10):
    if check[i]==False:
        count+=1
if count == 0:
    print('None')
else :
    cnt = 0
    for i in range(10):
        if check[i]==False:
            print(i,end='')
            cnt +=1
            if cnt != count:
                print(',', end='')
    