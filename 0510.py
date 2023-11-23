def cut(lst):
    lst1 = []
    lst2 = []
    [lst1.append(lst[a]) for a in range(int(len(lst)/2))]
    [lst2.append(lst[int(len(lst)/2)+a]) for a in range(int(len(lst)/2))]
    
    return lst2 + lst1

def slice(lst):
    newList = []
    for i in range(int(len(lst)/2)):
        newList.append(lst[i])
        newList.append(lst[i + int(len(lst)/2)])
    return newList

card = input().split()

order = input()
for i in order:
    if i == 'C':
        card = cut(card)
    if i == 'S':
        card = slice(card)

[print(i, end=' ') for i in card]