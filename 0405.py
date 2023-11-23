true = input()
answer = input()

count=0
if len(true)==len(answer):

    for i in range(len(true)):
        if true[i]==answer[i]:
            count+=1
    print(count)
else :
    print('Incomplete answer')