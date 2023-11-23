
def grade_mcq(sol, ans):
    true = sol
    answer = ans
    count=0
    if len(true)==len(answer):

        for i in range(len(true)):
            if true[i]==answer[i]:
                count+=1
        return count
    else :
        return -1
    
exec(input())