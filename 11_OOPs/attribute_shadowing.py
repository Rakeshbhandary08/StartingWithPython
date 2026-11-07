class Student:
    name="Rakesh";
    course="BCA"

student1=Student() #student1 will get all the attribute of Student class

student1.name="Mohit"
print(student1.name)
print(Student.name)

#Self Argument
class Person:
    height="short";
    skin="brown";

    def calling(self):
     print(f"A {self.height} man with {self.skin} skin")

#Create an instance of a class
person=Person()
person.height="tall"
Person.calling(person)


