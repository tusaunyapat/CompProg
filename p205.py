string1 = input().strip()
s1 = string1
string2 = input().strip()
s2 = string2
string1 = string1.lower()
string2 = string2.lower()

char1 = {}
char2 = {}
char = {}

for i in string1:
    if 97 <= ord(i) <= 122: 
        if i not in char1:
            char1[i] = 1
        else :
            char1[i] += 1
        if i not in char:
            char[i] = 1
        else :
            char[i] += 1
for i in string2:
    if 97 <= ord(i) <= 122: 
        if i not in char2:
            char2[i] = 1
        else :
            char2[i] += 1
        if i not in char:
            char[i] = 1
        else :
            char[i] += 1

remove1 = []
remove2 = []
for i in char:
    if i not in char1:
        char1[i] = 0
    if i not in char2:
        char2[i] = 0
    
for i in char:
    if char1[i] > char2[i] :
        remove1.append([i,char1[i] - char2[i]])
    if char2[i] > char1[i] :
        remove2.append([i, char2[i] - char1[i]])
remove1.sort()
remove2.sort()
#print
print(s1)
if len(remove1) != 0:
    for i in remove1:
        if i[1] > 1:
            print(' - remove',i[1],str(i[0])+'\'s')
        else :
            print(' - remove',i[1],i[0])
else :
    print(' - None')
print(s2)
if len(remove2)!= 0:
    for i in remove2:
        if i[1] > 1:
            print(' - remove',i[1],str(i[0])+'\'s')
        else :
            print(' - remove',i[1],i[0])
else :
    print(' - None')




