def change(sec):
    minute = sec//60
    sec -= minute*60
    sec = int(sec)
    if sec < 10:
        sec = '0'+str(sec)
    return str(minute)+':'+str(sec)

n = int(input())
d = {}
for i in range(n):
    data = input().split(',')
    Type = data[2].strip()
    minute, sec = data[3].split(':')
    time = int(minute)*60 + int(sec)
    if Type not in d:
        d[Type] = time
    else :
        d[Type] += time

newDict = {}
for i in d:
    value = d[i]
    newDict[value] = i

top = sorted(newDict)[::-1]
print(newDict)
count = 0
for i in top:
    print(newDict[i],'-->',change(d[newDict[i]]))
    count += 1
    if count == 3:
        break
