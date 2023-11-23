search = input()
text = input()
count = 0

for i in range(len(text)-len(search)):
    for j in range(len(search)):
        if search[j]!=text[i+j]:
            break
        if j == len(search)-1:
            count+=1

print(count)
