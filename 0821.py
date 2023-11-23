string = input()
string = string.lower()

alp = {}
data = []

for i in string:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in alp:
            alp[i] = -1
        else :
            alp[i] -= 1

[data.append([alp[i], i]) for i in alp]
data.sort()

for i in range(len(data)):
    print(data[i][1], '->', -data[i][0])
