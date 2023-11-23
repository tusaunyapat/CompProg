n = int(input())
menu = {}

for i in range(n):
    name, cost = input().split()
    menu[name] = int(cost)
money = 0

each_menu = {}
m = int(input())
for i in range(m):
    name, num = input().split()

    if name in menu:
        if name in each_menu :
            each_menu[name] += int(num) * menu[name]
        else :
            each_menu[name] = int(num) * menu[name]

# print(each_menu)
ls_final = []
[ls_final.append([i, each_menu[i]]) for i in each_menu]
most = 0
ls_final.sort()
cost = 0
for i in range(len(ls_final)):
    cost += ls_final[i][1]
    if ls_final[i][1] > most:
        most = ls_final[i][1]
        name_most = ls_final[i][0]
    elif ls_final[i][1] == most:
        name_most += ', ' + ls_final[i][0] 

if len(ls_final) == 0:
    print('No ice cream sales')
else :
    print('Total ice cream sales:', float(cost))
    print('Top sales:',name_most)

