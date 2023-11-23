idol = {}
ota = {}

while True:
    raw = input().split()
    if len(raw) == 1:
        option = raw[0]
        break

    fc, mb, sc = raw[0], raw[1], (int(raw[2])*-1)
    #idol
    if mb not in idol:
        idol[mb] = {}
        idol[mb]['score'] = 0
        idol[mb]['from'] = []
        idol[mb]['be_cami'] = 0
    idol[mb]['score'] -= sc
    if fc not in idol[mb]['from']:
        idol[mb]['from'].append(fc)

    #ota
    if fc not in ota:
        ota[fc] = []
    ota[fc].append([sc,mb])

if option == '1':
    wait = []
    for mb in idol:
        wait.append([(-1*idol[mb]['score']), mb])
    wait.sort()
    ans = wait[0][1] +', ' + wait[1][1] + ', ' + wait[2][1]
    print(ans)

if option == '2':
    wait = []
    for mb in idol:
        wait.append((len(idol[mb]['from']), mb))
    wait.sort()
    ans = wait[-1][1] +', ' + wait[-2][1] + ', ' + wait[-3][1]
    print(ans)

if option == '3':
    fan = sorted(ota)
    # print(fan)
    for fc in fan:
        ota[fc].sort()
        # print()
        idol[ota[fc][0][-1]]['be_cami'] += 1
    
    member = sorted(idol)
    wait = []
    for i in member:
        wait.append([idol[i]['be_cami'], i])
    wait.sort()
    ans = ''
    ans = wait[-1][1] +', ' + wait[-2][1] +', ' + wait[-3][1]
    print(ans)


print(idol)

