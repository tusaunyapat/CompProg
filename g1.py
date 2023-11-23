# ให้เขียนโปรแกรมในบริเวณที่กำหนดในเซลล์นี้เท่านั้น ห้ามลบ/แก้ไข ข้อความที่เตรียมไว้ให้



def generate_seating_sequence(group1,group2,seats_p_row):
  # เขียนโปรแกรมในส่วนนี้
    seating_sequence = [" -"] * 4 * seats_p_row
    seating_sequence[0:len(group1) * 2:2] = group1
    seating_sequence[1:len(group2) * 2:2] = group2
    # print(seating_sequence)

    return seating_sequence
#------------------------------------------------------------#    
def group_reverse_order(group):
  # เขียนโปรแกรมในส่วนนี้
    reverse_group = group[::-1]


    return reverse_group 
#------------------------------------------------------------#    
def display_exam_seating(seating_sequence):
  # เขียนโปรแกรมในส่วนนี้
    num = len(seating_sequence)//4

    print('-'*int(num*3+1))
    print('|'+' '*int(((num*3)-10)/2)+'Exam room'+' '*int(((num*3)-10)/2)+'|')
    print('-'*(num*3+1))
    print('|'+'|'.join(seating_sequence[:num])+'|'+'\n'+'-'*(num*3+1))
    print('|'+'|'.join(seating_sequence[num:num*2])+'|'+'\n'+'-'*(num*3+1))
    print('|'+'|'.join(seating_sequence[num*2:num*3])+'|'+'\n'+'-'*(num*3+1))
    print('|'+'|'.join(seating_sequence[num*3:num*4])+'|'+'\n'+'-'*(num*3+1))
    return


#------------------------------------------------------------#    
def main():
    group1 = input().split(",") # A1,A2,A3
    group2 = input().split(",") # C1,C2,C3,C4
    seats_p_row = int(input())  # 4, 6, 8, 10
    is_reverse = int(input())  # 0, 1
    
    if is_reverse:
        group1 = group_reverse_order(group1)
        group2 = group_reverse_order(group2)
        
    if len(group1) > 2*seats_p_row or len(group2) > 2*seats_p_row:
        print("Room is too small. Get a bigger exam room!")
        return
    
    if seats_p_row < 4 or seats_p_row % 2 != 0:
        print("seats_p_row has to be more than 4 and has an even number.")
        return
    
    seating_sequence = generate_seating_sequence(group1,group2,seats_p_row)
    display_exam_seating(seating_sequence)

main()
