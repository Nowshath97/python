a = 10

def func():
    global a
    a=15
    print(a)

func()
print(a)

x=20
def glob():
    y =globals()['x']
    globals()['x']=30
    print(y)

glob()
print(x)



def count(lst):
    e = 0
    o = 0
    for i in lst:

        if i%2 == 0:
            e+=1
        else:
            o+=1
    return e,o

lst = [20,15,14,17,24,12,13,19,28]
even,odd = count(lst)
print("Even:{} and Odd:{}".format(even,odd))

names = ['Rohit','Gill','Kohli','Rahul','Pandya','Dube','Bumrah','Kuldeep','SuryaKumar','Arshdeep']

def name_len(names):
    lencount = 0
    for i in names:

        if (len(i))<=5:
            lencount = lencount+1
    return lencount

x = name_len(names)
print(x)

def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

fib(5)


def fact(n):
    a=1
    for i in range(1,n):
        a=a*i
    print(a)

fact(4)

def recur(n):
    if n==0:
        return 1
    return n * recur(n-1)

print(recur(5))