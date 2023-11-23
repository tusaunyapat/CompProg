tel = input()

if tel[0] == '0' :
    if tel[1] == '6' or tel[1] == '8' or tel[1] == '9':
        print('Mobile number')
    else :
        print('Not a mobile number')
else :
    print('Not a mobile number')