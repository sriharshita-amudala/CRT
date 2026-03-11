'''li=[1,2,3,4,5]
output=[2,4,6,8,10]

li=list(map(int,input().split()))
res=[]
for i in li:
    res.append(i*2)
print(res)
print(i*2 for i in li)
 

li=[1,2,3,4,5]
#output=[2,4]
res=[]
for i in li:
    if i%2 ==0:
        res.append(i)
print(res)
print(i for i in li if i%2 ==0)

#['a', 'b', 'c',] ==>"abc"
li1=['a', 'b', 'c']
res=""
for i in li1:
    res+=i
print(res)
print("".join(li1))'''

'''Intermediate patterns:
1.Pyramid pattern
n=4
output:
   *
  * *
 * * *
* * * *   

n=int(input())  
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()  '''

'''2. Inverted pyramid pattern
n=4
output:
    * * * * 
     * * *
      * *
       *'''

'''n=int(input())
for i in range(n,0,-1):
    for j in range()'''
