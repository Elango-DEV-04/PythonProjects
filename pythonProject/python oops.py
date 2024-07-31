'''class person:
 def __init__(self,name,age):
    self.name = name
    self.age  = age
p1 = person("sathis",22)
p2 = person("control",66)
print(p1.name,p1.age)
print(p2.age,p2.name)


class Person:
  def __init__(sumi, fname, lname):
    sumi.firstname = fname
    sumi.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
x = Person("John", "Doe")
x.printname()'''

'''class Animal:
    def speak(self):
        print("Animal Speaking")
#child class Dog inherits the base class Animal
class Dog(Animal):
    def bark(self):
        print("dog barking")
d = Dog()
d.bark()
d.speak()

d1 = Dog()
d1.bark()
d1.speak()'''


class Calculation1:
    def add(self,a,b):
        return a+b;
class Calculation2:
    def Multiplication(self,a,b):
        return a*b;
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a/b;uu
d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))