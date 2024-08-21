list=[6,0,3,5,7]


def bubsort(list):
    n=0
    l = len(list)-1
    while n<l:
        if list[n]>=list[n+1]:
            temp = list[n]
            list[n]=list[n+1]
            list[n+1]=temp
        n+=1

bubsort(list)

print(list)