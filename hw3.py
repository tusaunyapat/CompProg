def get_sid_section(stu_rec):
    student = stu_rec.split(',')
    return [student[0], str(int(student[1]))]

def get_sid_sections(stu_recs):
    answer = []
    for i in stu_recs:
        answer.append(get_sid_section(i))
    answer.sort()
    return answer

def get_section(sid_sections, sid):
    found = False
    for i in range(len(sid_sections)):
        if sid_sections[i][0] == sid :
            found = True
            break
    return sid_sections[i][1] if found else '0'

def get_stu_points(grader_points):
    data = [e for e in grader_points]
    data.sort()
    for i in range(len(data)):
        data[i] = data[i].split(',')
    name = data[0][0]
    maxScore = int(data[0][2])
    answer = []
    for i in range(len(data)):
        if data[i][0] == name :
            if maxScore < int(data[i][2]):
                maxScore = int(data[i][2])
        else :
            answer.append([name, maxScore])
            name = data[i][0]
            maxScore = int(data[i][2])
    answer.append([name, maxScore])
    return answer


def get_stu_section_points(stu_points, sid_sections):
    answer = []
    student = []
    
    for i in range(len(stu_points)):
        sid = stu_points[i][0]
        section = get_section(sid_sections, sid)
        answer.append([section, stu_points[i][1], sid])

    return answer
        
def get_section_point_count(stu_section_points, min_point):
    data = [e for e in stu_section_points]
    data.sort()
    # print(data)
    section = data[0][0]
    count = 0
    answer = []
    for i in range(len(data)):
        if data[i][0] == section:
            if data[i][1] >= min_point:
                count += 1
        else :
            answer.append([section, count])
            count = 0
            if data[i][1] >=min_point :
                count+=1
            section = data[i][0]
    answer.append([section, count])
    return answer

print(get_section_point_count([["101", 100, "Lalisa"], ["0", 0, "Luffy"], ["7", 100, "MrBond"], 
     ["7", 0, "Zoro"], ["101", 60, "stu_CompProg"]], 60))