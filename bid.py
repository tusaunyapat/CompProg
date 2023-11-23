n = int(input()) 
product = {} 
buy = {} 
for i in range(n): 
    x = input().strip().split() 
    if x[0] == 'B': 
        buyer,pro,price = x[1:] 
        price = int(price) 
        if pro in product: 
            if price in product[pro]: 
                product[pro][price].append(buyer) 
            else: 
                product[pro][price] = [buyer] 
        else: 
            product[pro] = {price:[buyer]} 
        if buyer in buy: 
            buy[buyer].append([pro,price]) 
        else: 
            buy[buyer] = [[pro,price]] 
    elif x[0] == 'W': 
        buyer,pro = x[1:] 
        for e in product[pro]: 
            if buyer in product[pro][e]: 
                product[pro][e].remove(buyer) 
        for e in buy[buyer]: 
            if e[0] == pro: 
                buy[buyer].remove(e) 
out = {} 
for e in product: 
    bp = product[e] 
    x = [a for a in bp.keys() if bp[a] != []] 
    if x != []: 
        pmax = max(x) 
        wb = bp[pmax][0] 
        if wb in out: 
            out[wb][0] += pmax 
            out[wb][1].append(e) 
        else: 
            out[wb] = [pmax,[e]] 
outr = [] 
for e in buy: 
    if e in out: 
        outr.append([e,out[e][0],out[e][1]]) 
    else: 
        outr.append([e,0,[]]) 
outr.sort() 
for b,p,pp in outr: 
    if p > 0: 
        pp.sort() 
        print((b+': $'+str(p)+' -> '+' '.join(pp)).strip()) 
    else: 
        print(b+': $'+str(p))