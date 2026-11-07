def greet(name,age):
    print(name,age)

#greet(age=100,name='Rakesh')

#Default Arguments
def calling(name='Guest'):
    print(f"You are {name}")

# calling('Rakesh')
# calling()

#Arbitrary positional arguments
def position(*args):
    print(args)

#position(10,20,40,50)

#addition
def add(*args):
    sum=0;

    for arg in args:
        sum=sum+arg

    return sum

#print(add(10, 20, 30, 40, 50,80,45,12))

#Accept multiple name argument

def student(**values):
    print(values)

#student(name="Rakesh",course="BCA",year=3)
main=0;
def update(num): #num=10
    num = 100
    main=num

value = 10 #value=10

update(value)

print(value)
print(main)