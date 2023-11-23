n = int(input())
page = {}
for i in range(n):
    name = input()
    page[name] = input().split()

#word repeat
number = {}
for name in page:
    # print(name)
    num = 0
    done = []
    for word in page[name]:
        if word not in done:
            done.append(word)
            # print(word)
            num += 1
    number[name] = num

a = input()
ans = []
while a != '-1':
    
    maxx = 0
    for name in page:
        cnt = page[name].count(a)
        score = cnt / len(page[name]) / number[name]
        if score > maxx: 
            maxx = score
            read = name
    if maxx == 0:
        print('NOT FOUND')
    else:
        print(read)
    a = input()





