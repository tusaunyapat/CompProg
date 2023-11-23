def peaks(data):
    # data = [int(e) for e in input().split()]
    answer = []
    for i in range(1,len(data)-1,1):
        if data[i]>data[i+1] and data[i]> data[i-1]:
            answer.append(i)
            # print(data[i])
            # print(data[i-1:i+2])
    return answer

exec(input())