#Create a class
class Name():
    pass;

print(type(Name)) #It is a class

class duplicate():
    pass;

#Create a object using class
rakesh=Name()

print(type(rakesh))
print(type(rakesh) is duplicate)



#First class

class Student():
    pass;

student1=Student()
student1.name="Rakesh"
student1.course="BCA"
print(student1)


#Adding method to a class
class Greet:

    def calling(self):
        print("Namastey Rakesh")

store=Greet()
store.calling()