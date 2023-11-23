n = int(input())
actor = {}

for i in range(n):
    data = input().split(', ')
    name = data[0]
    act1 = data[1]
    act2 = data[2]

    if act1 not in actor:
        actor[act1] = ''
    if act2 not in actor:
        actor[act2] = ''
    actor[act1] += name+', '
    actor[act2] += name+', '

find = input().split(', ')
for act in find:
    if act in actor:
        print(act,'->',actor[act][:-2])
    else:
        print(act,'->','Not found')


