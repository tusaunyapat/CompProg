ally = {}

data = input().split()
while data[0] != 'End':
    if data[0] == 'Ally':
        for i in range(1, len(data)):
            if data[i] not in ally:
                ally[data[i]] = {}
            ally[data[i]] = ally[data[i]] | set
