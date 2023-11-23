import math

def distance1(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def distance2(p1, p2):
    x1 = float(p1[0])
    y1 = float(p1[1])
    x2 = float(p2[0])
    y2 = float(p2[1])
    return distance1(x1, y1, x2, y2)

def distance3(c1, c2):
    d3 = distance2(c1, c2)
    # print(d3, c1[2], c2[2])
    if d3 <= float(c1[2]) + float(c2[2]):
        overlap = True
    else :
        overlap = False
    return d3,overlap

def perimeter(points):
    length = 0
    for i in range(len(points)):
        # print(length)
        length += distance1(points[i][0],points[i][1],points[i-1][0],points[i-1][1])
    return length

exec(input().strip())