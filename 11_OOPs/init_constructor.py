
#Special method
class Student:
    def __init__(self,name,age,course):
        self.name=name;
        self.age=age;
        self.course=course
        print(f"Your name is {self.name} and your age is {self.age} from {self.course} course")

#Create a instance of class
student1=Student("Rakesh",22,'BCA')
student2=Student('Dexter',35,'MBBS')
print(student1.course)