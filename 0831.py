def total(pocket):
    cost = 0
    for key in pocket:
        cost += pocket[key] * key
    return cost

def take(pocket, money):
    for key in money:
        if key in pocket:
            pocket[key] += money[key]
        else:
            pocket[key] = money[key]
    return pocket

def pay(pocket, amt):
    money = {}
    for key in sorted(pocket.keys())[::-1]:
        
        if amt >= key:
            c = min(amt//key, pocket[key])
            
            money[key] = c
            pocket[key] -= c
            amt -= key * c
            
    if amt > 0:
        take(pocket,money)
        money = {}
    
    return money 
             
exec(input().strip())