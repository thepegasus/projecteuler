def checkfac(num):
    for j in range(11,20):
        if(num%j!=0):
            return False
    return True

for i in range(9999999,99999999):
    if(checkfac(i)):
        print(str(i))
        break;
    else:
        print(str(i)+" Not applicable ")

