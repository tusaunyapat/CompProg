def is_mobile_number(tel):
    if len(tel)!=10:
        return False
    else :
        if tel[0] == '0' :
            if tel[1] == '6' or tel[1] == '8' or tel[1] == '9':
                return True
            else :
                return False
        else :
            return False

exec(input())