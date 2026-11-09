#Basic composition

class Engine:
    def start(self):
        print("Engine has started")

class Car(Engine):
    def __init__(self):
        print("It is a  Car")
        #varible that contain all the functions of Engine Class

    

car1=Car() #{engine:classEngine(),}
car1.start()


#ANother Example


class Address:

    def __init__(self, city, state):
        self.city = city
        self.state = state

    def display_address(self):
        print("City:", self.city)
        print("State:", self.state)


class Student:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display_student(self):
        print("Student:", self.name)
        self.address.display_address()


address1 = Address("Gurugram", "Haryana") #{city:Gurugram,state:Haryana}

student1 = Student("Rakesh", address1) #{name:Rakesh,address,address:{city:Gurugram,state:Haryana}}

student1.display_student()
