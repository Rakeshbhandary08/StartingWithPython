fruits = ["apple", "banana", "mango", "orange"]

#Print all fruits
for fruit in fruits:
    print(fruit)


#Range return a range not a list or somthing
arr=[]
store=range(10) #{0,10}
print(list(store))

for item in range(10):
    arr.append(item)

print(f"Here is our created array {arr}")


numbers = [10, 20, 30, 40, 60, 100]

#Print the Indexes
for index in range(len(numbers)):
    print(numbers[index])

#Enumerate ->index and value

for idx,val in enumerate(numbers):
    print(idx,val)

