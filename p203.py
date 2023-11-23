def convex_polygon_area(p):
    area = 0
    for i in range(len(p)):
        if i == len(p)-1:
            area += p[i][0] * p[0][1]
            area -= p[i][1] * p[0][0]
        else :
            area += p[i][0] * p[i+1][1]
            area -= p[i][1] * p[i+1][0]
    area = 0.5 * abs(area)
    return area
def is_heterogram(s):
    s = s.lower()
    for i in s:
        if i not in "'' ,\{}":
            cnt = s.count(i)
            if cnt > 1: return False
    return True
def replace_ignorecase(s, a, b):
    newS = s.lower()
    a = a.lower()
    new = ''
    i = 0
    while i != len(s):
        text = newS[i:len(a)+i]
        if text == a:
            new += b 
            i += len(a)
        else :
            new += s[i]
            i += 1
    return new
def top3(votes):
    c = []
    score = []
    ans = []
    for i in votes:
        c.append([i, votes[i]])
        score.append(votes[i])
        c.sort()
    score.sort(reverse=True)
    for i in range(3):
        point = score[i]
        for j in c:
            if j[1] == point and j[0] not in ans:
                ans.append(j[0])
                break
    return ans


for i in range(2):
    exec(input().strip())


