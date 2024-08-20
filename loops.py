from array import *
x =0

while x<5:
    k=x
    print("Python",end="")
    while k<=x:
        print(" is powerful language")
        k=k+1
    x=x+1

p = 20
temp=0
for i in range(1,14):
    if p%i == 0:
        temp=temp+1

if temp<=2:
    print("p is a prime number")
else:
    print("p is not a prime number")

arr = array('i',[5,4,1,9,3])



newArr = array(arr.typecode,(b*b for b in arr))
for i in range(len(newArr)):
    print(newArr[i])