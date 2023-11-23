text = input()
char = text[0]

count = 0
for i in range(len(text)):
    if char == text[i]:
        count+=1
    else :
        print(char, count, end = ' ')
        char = text[i]
        count = 1
print(char, count)