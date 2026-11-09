# class Calculator:
#     @staticmethod
#     def addition(a,b):
#         return a+b

    
    

# add=Calculator() #Creating an instance of Calculator class
# print(Calculator.addition(10,48))
# print(add.addition(90,78))


# #@staticmethod isn't about making class-based function calls possible. It's about explicitly defining a method that doesn't require automatic instance or class binding.


#Properties - Getter Setter
class Employee:
    def __init__(self,name,salary):
        self.name=name;
        self._salary=salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,salary):
        if salary > 0:
            self._salary=salary
        else:
            print("Invalid Salary")

    

emp1=Employee("Rakesh",1000);


print(emp1.salary)
emp1.salary=-1000;
print(emp1.salary)