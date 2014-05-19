#The sum of the squares of the first ten natural numbers is, 12 + 22 + ... + 102 = 385
#The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
totsum=0
sqsum=0
for i in range(1,101):
    totsum+=i;
    sqsum+=(i*i);
    print(str(i)+" ^2+")
totsumsq=totsum*totsum
diff=totsumsq-sqsum
print("Total Sum: "+str(totsum)+" Sum of squares: "+str(sqsum)+" Difference:  "+str(diff))
