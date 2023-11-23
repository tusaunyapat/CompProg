filename = input()
function = input()
fn = open(filename, 'r')
textList = []
useLength = 100000
for line in fn:
    get = line.strip()
    textList.append(get)

def find_use(textList, function):
    useLength = 1000000
    for test in textList:
        if function == 'RSTRIP':
            test = test[::-1]

        for i in range(len(test)):
            if test[i] != '.' and useLength>i:
                useLength = i
    return useLength

def LSTRIP(textList, useLength):
    ans = []
    for i in textList:
        ans.append(i[useLength:])
    return ans

def RSTRIP(textList, useLength):
    ans = []
    for i in textList:
        ans.append(i[:len(i)-useLength])
    return ans

def STRIP(textList):
    ans = LSTRIP(textList, find_use(textList, 'LSTRIP'))
    ans = RSTRIP(ans, find_use(ans, 'RSTRIP'))
    return ans

def ALL(textList):
    index = []
    for i in textList:
        wait = set()
        for j in range(len(i)):
            if i[j] == '.':
                wait.add(j)
        index.append(wait)
    point = index[0]
    for i in index:
        point = point & i
    # print(point)
    ans = []
    for i in range(len(textList)):
        newtext = ''
        for j in range(len(textList[0])):
            if j not in point:
                newtext += textList[i][j]
        ans.append(newtext)
    return ans


if function == 'LSTRIP':ans = LSTRIP(textList, find_use(textList, 'LSTRIP'))
elif function == 'RSTRIP':ans = RSTRIP(textList, find_use(textList, 'RSTRIP'))
elif function == 'STRIP':ans = STRIP(textList)
elif function == 'STRIP_ALL': ans = ALL(textList)
else:print('Invalid command')

    
if function in ['LSTRIP', 'RSTRIP', 'STRIP', 'STRIP_ALL']:
    [print(i) for i in ans]
