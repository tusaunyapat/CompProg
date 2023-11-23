name = ['Robert','William','James','John','Margaret','Edward','Sarah','Andrew','Anthony','Deborah']
nickname = ['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']
answer =  []
num = int(input())

for i in range(num):
    want = input()
    # print('want = ',want)
    if want in name:
        ans = name.index(want)
        answer.append(nickname[ans])
    elif want in nickname:
        ans = nickname.index(want)
        answer.append(name[ans])
    else :
        answer.append('Not found')

[print(i) for i in answer]
