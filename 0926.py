n = int(input())
listOfID = []
listOfTown = []

for i in range(n):
    ID, town = input().split(':')
    town = town.strip()
    listOfID.append(ID)
    listOfTown.append(town.split(', '))
keyID = input()

index = listOfID.index(keyID)
town_keyID = set(listOfTown[index])

found = False
for i in range(len(listOfID)):
    if listOfID[i] != keyID:
        if len(town_keyID & set(listOfTown[i])) != 0:
            print(listOfID[i])
            found = True
if not found:
    print('Not Found')
                