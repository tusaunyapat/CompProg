summ = 0
n = int(input())
for i in range(n):
    a, b, c = [float(e) for e in input().split()]
    # print((b-a)*c)
    summ += (b-a+1)*c

print(summ/11)