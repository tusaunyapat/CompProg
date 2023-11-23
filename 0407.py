check = input()
string = input()
a = ''
count = 0
for c in string:
    if c in ['"', "'", '(', ')', ',', '.']:
        a += ' '
    else :
        a += c
a = a.split()
for c in a:
    if c == check:
        count+=1
print(count)