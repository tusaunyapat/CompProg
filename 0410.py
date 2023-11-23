string = input()
a = string[0]
count = 0
for i in range(len(string)):
    # print('a = ',a)
    if string[i]==a:
        count+=1
    else :
        print(a, count,end=' ')
        a = string[i]
        count = 1

print(a, count, end=' ')