#Basic Inheritance

# class Employee:
#     def __init__(self,name,age):
#         self.name=name;
#         self.age=age;

#     def display(self):
#         print(f"Hello {self.name} and your age is {self.age}")

# #Child class -> Addition information(super)
# class Developer(Employee):

#     def __init__(self,name,age,language):
#         super().__init__(name,age) #Inheritance

#         #Add additional information
#         self.language=language  #Add

#     def calling(self):
#         print(f"Additional Info: {self.language}")

#     pass;

# developer1=Developer('Rakesh',22,'Javascript')  #{name='rakesh',age='22',langage='javascript'}
# developer1.display()
# developer1.calling()


#Method Overriding

# class User:
#     def login(self):
#         print("User is logged in")

# class Admin(User):
#     def login(self):
#         super().login()
#         print("Admin is logged in")
#     pass;

# #User instance
# user1=User()
# user1.login()

# admin1=Admin();
# admin1.login()

#1-Single Inheritance(done)
#2-Multiple Inheritance(done)
# class Father:
#     def height(self):
#         print("Father's Height")

# class Mother:
#     def beauty(self):
#         print("Mother's Beauty")

# class Child(Father,Mother):
#     pass;

# child1=Child()
# child1.height()
# child1.beauty()

#3-MultiLevel Inheritance
# class GrandFather:
#     def myself(self):
#         print("I am the GrandFather")

# class Father(GrandFather):
#    def myselff(self):
#        print("I am the Father")

# class Child(Father):
#     pass;

# child1=Child();
# child1.myselff()
# child1.myself();

#4-Hierarchical Inheritance - Multiple child can have same parent
class Eat:
    def Eating(self):
        print("Eating")

#First chiild
class Dog(Eat):
    pass;

class Cat(Eat):
    pass;

class Rat(Eat):
    pass;


dog1=Dog()
dog1.Eating()

cat1=Cat()
cat1.Eating()

rat1=Rat()
rat1.Eating()

#5-Hybrid Inheritance

class A:
    def show(self):
        print("Class A")


class B(A):  #Heirarchical
    pass


class C(A):
    pass


class D(B, C):#multiple Inheritance
    pass


obj = D()
obj.show()