# for i in range(5):
#     print("Good morning students!")

# i=1
# while i<=5:
#     print("Good morning students!")
#     i+=1

# def greet():
#     print("hello students")
#     print("welcome to python programming")

# greet()
# def add(a,b):
#     result= a + b
#     print(result)
# add(10,20)
# add(50,30)    

# students = ["navya","priya","laya","maya"]
# students.append("pavan")
# students.remove("priya")
# students.insert(3,"don")
# print(students)
#######################tuple#############################

# student_details=("nabi",24,89.0,True)


# print(student_details[0])


#################dictionary##############

# student={
#     "name":"lakshmi",
#     "USN":"1GD24CI024",
#     "dept":"AIML",
#     "marks":98
# }
# student["course"]="python programming"
# student["marks"]=90
# print(student["name"])
# print(student["USN"])
# print(student["course"])

###################class & objects###############

# class student:
#     def display(self):
#         print("hello students")
#         print("welcome to python programming")


# s1=student()

# # s1.display()

# class student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks

#     def display(self):
#         print("Name:",self.name)
#         print("age:",self.age)
#         print("marks:",self.marks)

# s1=student("navi",20,40)
# s2=student("laks",70,90)        


# s1.display()
# s2.display()


# class student:
#     def __init__(self):
#         self._marks = 0

#     def set_marks(self,marks):
#         self._marks = marks

#     def show_marks(self):
#         print("student marks:",self._marks)

#         s1 = student()
#         s1.set_marks(85.6)
#         s1.show_marks()        
# class grandfather:
#     def land(self):
#         print("grandfather has a land")

# class father(grandfather):
#     def house(self):
#         print("father has a house")

# class son(father):
#     def car(self):
#         print("son has a car")

# class daughter(father):
#     def thar car(self):
#         print("daughter has thar car")        

# s = son()
# s.land()
# s.house()
# s.car()
# s.thar car()        
##########################polymorphism############################

# class Animal:
#     def sound(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def sound(self):
#         print("Dog barks")
# class Cat(Animal):
#     def sound(self):
#         print("Cat meows")

# animals = [Dog(),Cat(),Animal()]
# for animal in animals:
#     animal.sound()                        

##################abstract##############

from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class UPI(payment):
    def pay(self,amount):
        print(f"Paid {amount} using UPI")

class Card(payment):
    def pay(self,amount):
        print(f"Paid {amount} using Card")

p1 = UPI()
p2 = Card()
p1.pay(1000)
p2.pay(2000)                        