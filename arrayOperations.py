from numpy import *

arr1 = array([4,7,9,3,1])
arr2 = array([5,2,0,6,8])
print(arr1)
arr1[2] = 10
arr2 = arr1.view()
arr1[2] = 8
print(arr2)
arr2 = arr1.copy()
arr1[2] = 10
print(arr2)
arr = linspace(0,15,10)
logarray = logspace(0,15,10)

arr3 = arange(15,1,-2)
arr4 = arange(15,2,-3)
arr5 = arr1+5
arr6 = arr1 + arr2

print(arr)
print(logarray)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(log(arr1))