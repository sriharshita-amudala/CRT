import numpy as np

arr=np.array([10,20,30,40,50])
print("Array Elements:",arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr)) 
print(np.sum(arr))
print(np.zeros(5))
print(np.ones(8))
print("Even Numbers:",np.arange(2,10,2))
print("Odd Numbers:",np.arange(1,10,2))

n=int(input("Enter size of array:"))
ele=list(map(int,input("Enter elements:").split()))
print("User Defined Array:",np.array(ele))
print("Sorted Array:",np.sort(arr))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     


import array
arr=array.array('i',[])
print(arr,type(arr))
arr.append(10)
arr.append(20)  
print(arr)