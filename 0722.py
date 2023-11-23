first = input().lower()
second = input().lower()

F = []
S = []

for i in range(len(first)):
    if first[i] != ' ':
        Ascii = ord(first[i])
        F.append(Ascii)

for i in range(len(second)):
    if second[i] != ' ':    
        Ascii = ord(second[i])
        S.append(Ascii)
F.sort()
S.sort()
# print(F)
# print(S)
print("YES") if F == S else print("NO")

