def first_fit(L, e):
    for i in range(len(L)):
        if sum(L[i])+e <= 100:
            L[i].append(e)
            return L
    L.append([e])
    return L

def best_fit(L, e):
    dif = 100
    for i in range(len(L)):
        if 100 - (sum(L[i]) + e)  <= dif:
            if 100 - (sum(L[i]) + e)>= 0:
                dif = 100 - (sum(L[i]) + e)
                index = i
            # if dif<0:
            #     dif=100
            # print(dif)
    print(dif)
    if dif != 100 :
        L[index].append(e)
    else :
        L.append([e])
    return L

def partition_FF(D):
    ans = []
    for i in range(len(D)):
        ans = first_fit(ans, D[i])
    return ans

def partition_BF(D):
    ans = []
    for i in range(len(D)):
        ans = best_fit(ans, D[i])
    return ans

exec(input().strip())