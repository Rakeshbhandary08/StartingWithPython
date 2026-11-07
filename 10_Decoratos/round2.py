#We want to execute something before and after greet() without modifying its original code.

def greet(name):
    print(f"Hello {name}")


def doSomething(func):

    def wrapper(*args):
        print("I am doing something before function")

        func(*args)

        print("I am doing something after function")

    return wrapper

store=doSomething(greet)
store('Acharya')
