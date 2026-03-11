'''INPUT: 12 
output: 1 2 3 4 6 '''

'''n=int(input("Enter a number:"))
print("Factors of",n,"are:")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=" ")''''''

input:12
output: 6(count of factors)

n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1    
print(count)

n=int(input("Enter a number:"))
counter=0
for i in range(1,n+1):
    if n%i==0:
        counter+=1
print("prime" if counter==0 else "not prime")

display prime numbers between the given range


start =int(input("Enter a number:"))
end = int(input("Enter a number:"))
if start<2:
    start=2
for n in range(start,end+1):
    counter=0
    for i in range(2,n//2+1):
        if n%i==0:
            counter+=1
    if counter==0:
        print(n,end=" ")
        
factorial of a number 
input: 5
output: 120

n=int(input("Enter a number:"))
if n<0:
    print("no factorial")
elif n==0 and n==1:
    print("factorial is 1")
else:
    fact=1
    for i in range(2,n+1):
        fact*=i
    print(fact)

GCD of two numbers
input: 12 15

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
while b:
    a,b=b,a%b
print(a)

import math
print(math.gcd(a,b))

fibonacci series
input: 10   
n=int(input("Enter a number:"))
a=0
b=1
count=0 

while count<n:
    print(a,end=" ")
    a,b=b,a+b
    count+=1
    '''
