string = input()
check = []

for i in range(len(string)):
    a = string[i]
    count = 0
    for i in range(i,len(string),1):
        if string[i] == a and a not in check:
            count+=1
    if count > 1:
        print(a,end='')
        check.append(a)
