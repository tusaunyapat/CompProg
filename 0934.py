def pattern1(nrows, ncols):
    ans = []
    n = 1
    for i in range(nrows):
        run = []
        for j in range(ncols):
            run.append(n)
            n += 1
        ans.append(run)
    return ans

def pattern2(nrows, ncols):
    ans = []
    for i in range(nrows):
        run = []
        for j in range(ncols):
            run.append((i+1) + nrows*j)
        ans.append(run)
    return ans

def pattern3(N):
    ans =  []
    n = 1
    for i in range(N):
        run = []
        for k in range(i):
            run.append(0)
        for j in range(N-i):
            run.append(n)
            n += 1
        ans.append(run)
    return ans

def pattern4(N):
    ans = []
    start = 1
    for i in range(N):
        run = []
        for k in range(i):
            run.append(0)
        n = start -1
        for j in range(N-i):
            n += + j + 1 + i
            run.append(n)
        ans.append(run)
        start += i
    return ans

def pattern5(N):
    ans = []
    start = 1
    for i in range(N):
        run = []
        for k in range(i):
            run.append(0)
        n = start
        for j in range(N-i):
            run.append(n)
            n += N - j
        start += 1
        ans.append(run)
    return ans

def pattern6(N):
    ans = []
    run = 1
    for i in range(N):
        ans.append([0]*i)
    
    for i in range(N):
        if i%2 == 0:
            for j in range(N-i):
                ans[j].append(run)
                run += 1
        else :
            for j in range(N-i,0,-1):
                ans[j-1].append(run)
                run += 1

    return ans





exec(input().strip())