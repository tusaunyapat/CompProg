name = ['Robert', 'William', 'James', 'John', 'Margaret', 'Edward', 'Sarah', 'Andrew', 'Anthony', 'Deborah']
nick = ['Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']
answer = []
n = int(input())
for i in range(n):
    a = input()
    if a in name:
        index = name.index(a)
        answer.append(nick[index])
    elif a in nick:
        index = nick.index(a)
        answer.append(name[index])
    else :
        answer.append('Not found')
[print(e) for e in answer]