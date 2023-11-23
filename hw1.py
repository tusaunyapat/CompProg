def center(r):
    xAxis = r[2]/2
    yAxis = r[3]/2
    answer = []
    answer.append(float(r[0])+xAxis)
    answer.append(float(r[1])-yAxis)
    return answer

def distance(r1,r2):
    p1 = center(r1)
    p2 = center(r2)
    diffX = (p1[0]-p2[0])**2
    diffY = (p1[1]-p2[1])**2
    answer = (diffX + diffY)**0.5
    return answer

def intersection(r1,r2):
    h_choice = []
    w_choice = []

    h_choice.append(r1[3]) # pic1 height
    h_choice.append(r2[3]) # pic2 height
    gap_up_y = abs(r1[1]-r2[1])
    gap_down_y = abs((r1[1]-r1[3])-(r2[1]-r2[3]))
    h_choice.append(abs(r2[1]-(r1[1]-r1[3])))
    h = max(h_choice) - gap_down_y - gap_up_y

    w_choice.append(r1[2]) # pic1 width
    w_choice.append(r2[2]) # pic2 width
    gap_right_x = abs(r1[0]-r2[0])
    gap_left_x = abs((r1[0]+r1[2])-(r2[0]+r2[2]))
    w_choice.append(r2[0]+r2[2]-(r1[0]))
    w_choice.append(r1[0]+r1[2]-(r2[0]))
    w = max(w_choice) - gap_left_x - gap_right_x
    h_choice.append(r1[1]-(r2[1]-r2[3]))
    
    return (abs(w*h)+(w*h))/2

def union(r1, r2):
    area1 = r1[2]*r1[3]
    area2 = r2[2]*r2[3]
    sumArea = area1 + area2
    unionArea = sumArea - intersection(r1,r2)
    return unionArea
    


def iou(r1,r2):
    return intersection(r1,r2)/union(r1, r2)

r1=[1.0, 4.0, 1.5, 2.0]
r2=[2.0, 5.0, 2.5, 2.0]
r3=[4.0, 5.5, 1.5, 3.5]
r4=[6.0, 4.5, 1.5, 2.0]
r5=[5.75, 7.0, 2.0, 5.0]


exec(input())

