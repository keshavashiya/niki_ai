import math
 
n = input("Enter number....")

def primeFactors(n):
     
    while n % 2 == 0:
        print 2,
        n = n / 2


    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            print i,
            n = n / i

    if n > 1:
        print n
 


def is_prime(n):
    x = True 
    for i in range(2, n):
       if n%i == 0:
           x = False
           break 

    if x:
        print "Number is prime"
    else:
        print "Number is not prime"



if n < 100000:
	is_prime(n)
	primeFactors(n)
else:
	print("Please enter no less then 100000")