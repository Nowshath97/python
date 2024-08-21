
def sum(a,b):
    c = a+b
    return c

print(sum(4,6))

def area(l,b):
    a = l*b
    print(a)

area(10,30)
area(10,10)

def avg( *b):
    c = 0
    for i in b:
        c=c+i
    print(c)

avg(5,2,4,6)


def person(name, *data):
    print(name)
    print(data)

person("Naushad",28,'Khammam','9848032919')

def person2(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person2("Naushad",age=31,city='Khammam',mobile=9848032919)