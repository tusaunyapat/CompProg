data = ''
d = {}
t = []
while data !='q':
    data = input()
    if data != 'q':
        name, Type = data.split(',')
        Type = Type.strip()
        if Type not in d:
            t.append(Type)
            d[Type] = []
        d[Type].append(name)


for i in t:
    print(i+':',', '.join(d[i]))

