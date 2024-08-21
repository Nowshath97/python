pos=-1

list=[5,8,7,3,2,6,4,1]

list.sort()

def search(list,n):
    low = 0
    up =  len(list)-1

    while low<=up:
        mid = (low+up)//2
        if list[mid]==n:
            pos = globals()['pos']=mid
            return True
        elif n<list[mid]:
            up=mid-1
        else:
            low=mid+1

n=6
if search(list,n):
    print("found at",pos)
else:
    print("Not found")