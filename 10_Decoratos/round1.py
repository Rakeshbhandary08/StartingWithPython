def greet():
    print("Hello world")

def welcome(func):
    func()

welcome(greet) #function passed as an argumnet in a function

#Returning a function from another function

def outer():
    print("I am outer")
    def inner():
     print("I am innner")

    return inner;

innerFunc=outer()
innerFunc()
