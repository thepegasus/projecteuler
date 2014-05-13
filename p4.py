
def factorise(num):
    for i in range(100, 999):
        if(num%i==0):
            print "================================"
            print "Factor found:"+str(i)
            divval=num/i
            if(divval>99 and divval<1000):
                print(str(num)+"="+str(divval))+"X"+str(i)
                return True
    return False
    
for i in range(999999,99999, -1):
    if(str(i)==str(i)[::-1]):
          print(str(i))
          if(factorise(i)):
              break;

