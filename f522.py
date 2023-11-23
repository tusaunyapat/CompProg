def index_of(grades, ID):
    for i in range(len(grades)):
        if grades[i][0] == ID:
            return i
    return -1

def upgrade(grades, ID):
    grade = ['A','B+','B','C+','C','D+','D','F']
    for i in ID:
        
        index = index_of(grades,i)
        if index != -1:    
            index2 = grade.index(grades[index][1])
                
            if index2!=0:
                    
                grades[index][1] = grade[index2-1]
    grades.sort()

exec(input())
exec(input())
exec(input())