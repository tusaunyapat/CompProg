def spiral_square(n):
    answer = []
    for i in range(n):
        wait = []
        for j in range(n):
            wait.append(0)
        answer.append(wait)
    xAxis = int(n//2 +1)
    yAxis = int(n//2 +1)
    route = []

    for i in range(n):
        if i%2==0:
            #L
            for j in range(i):
                route.append((0,-1))
            #D
            for j in range(i):
                route.append((1,0))
        if i%2==1:
            #R
            for j in range(i):
                route.append((0,1))
            #T
            for j in range(i):
                route.append((-1,0))
    for i in range(n-1):
        route.append((0,1))
    # print(route)
    run = 2
    answer[xAxis-1][yAxis-1] = 1
    
    for x,y in route:
        xAxis += x
        yAxis += y
        answer[xAxis-1][yAxis-1] = run
        run += 1
    return answer
    
def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

# exec(input().strip())

print_square(spiral_square(7)) 
