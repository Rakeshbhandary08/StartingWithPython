values=('Rakesh',22,'online',False,14500)

#tuple unpacking
name,age,mode,graduate,fees=values

print(f"Student name is {name} age {age} doing college in {mode} mode and fees is {fees} ")

print(values)
print(type(values))


fruits='apple','mango','banana','lichi'


#Compare tuple with list
list=['apple','mango','banana','lichi']
list[0]="grapes"
print(list)
print(type(fruits))
print(fruits[0:4])


numbers = (10, 20, 30, 10, 10, 40,10,10)

#Count the frequency of 10
print(numbers.count(10))

#Find the index of particular element like 40
print(numbers.index(40))

#Find the length
print(len(numbers))

#Membership -> checking the element is present or not
print(100 in numbers)
print(40 in numbers)


#Concatenation of tuple
vegetables='potato','tomato','carrot','ladyfinger'
price=20,40,65,90

print(vegetables)
print(price)

print(vegetables + price + fruits)


#Swapping using tuple

a=10;
b=20;

print(a,b)

#swap
a,b=b,a

print(a,b)