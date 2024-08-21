from array import *

arr = array('i',[5,4,1,9,3])

arr2 = array('i',[])

newArr = array(arr.typecode,(b*b for b in arr))
for i in range(len(newArr)):
    print(newArr[i])

n = int(input("Enter the number of items"))

for i in range(n):
    x = int(input("Enter the value "+ str(i+1) + ":"))
    arr2.append(x)

print(arr2)

s = int(input("Enter a number to search"))
#print(arr2.index(s))
for e in range(len(arr2)):
    if arr2[e]==s:
        print(e)
        break
else:
    print("Number not found")




