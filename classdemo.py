
class person:

    def __init__(self,name="No name",age=0):
        self.name=name
        self.age=age
    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False


p1=person()
p2 = person("Shezin",1)
p1.name="Naushad"
p1.age=1
print(p2.name)
print(p1.name)

if p1.compare(p2):
    print("They are same")
else:
    print("They are different")

class A:
    def feature1(self):
        print("Feature-1 working")
    def feature2(self):
        print("Feature-2 working")
class B:
    def feature1(self):
        print("Feature-1B working")
    def feature3(self):
        print("Feature-3B working")
class C(A,B):
    def feature4(self):
        print("feature-4 working")
    def feature5(self):
        print("feature-5 working")

a1 = C()
a1.feature4()
a1.feature3()
a1.feature1() # MRO 
