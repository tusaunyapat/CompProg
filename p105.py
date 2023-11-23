data = []
sum_par = 0
sum_stroke = 0
improve = []

for i in range(9):
    raw = [int(i) for i in input().split()]
    data.append(raw)
    sum_par += data[i][0]
    sum_stroke += data[i][1]

for i in range(9):
    if data[i][2]==1:
        # print(f'between {data[i][0]+2} and {data[i][1]}')
        get = min(data[i][0]+2, data[i][1])
        improve.append(get)

sum_improve = sum(improve)

tmp = ((sum_improve * 1.5) - sum_par) * 0.8
point = tmp // 1
point_net = sum_stroke - point

print(int(sum_stroke))
print(int(point))
print(int(point_net))