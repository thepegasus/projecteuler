#!/usr/bin/python3
#Problem 3 - Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

def checkPrime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
            
            
targetnum=600851475143/2
currentnum=2
while currentnum<targetnum:
    print("Checking:"+str(currentnum));
    if(targetnum%currentnum==0):
        if(checkPrime(currentnum)):
            print (str(currentnum))
    currentnum+=1
