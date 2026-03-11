''''n=int(input())
count=0
while n>0:
    count+=1
    n=n//10
print(count)
print(len(str(n)))'''

'''n=int(input())
temp=n  
s=0
while n>0:
    s+=n%10
    n=n//10
print(s)

print(sum(map(int,str(temp))))'''

'''n=int(input())
even=0
odd=0
while n>0:
    r=n%10
    if r%2==0:
        even+=1
    else:
        odd+=1
    n=n//10

print(even,odd)'''

'''n=int(input("Enter a number:"))
while n>9:  
    n=sum(map(int,str(n)))
print(n)'''



