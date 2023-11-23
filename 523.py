n = int(input())
data = []
dis = []
dis2 = []
for i in range(n):
    x, y = input().split()
    x = float(x)
    y = float(y)
    dis.append(((x**2)+(y**2))**0.5)
    dis2.append(((x**2)+(y**2))**0.5)
    data.append((x,y))

dis.sort()
index = dis2.index(dis[2])



print('#'+str(index+1)+':', data[index])