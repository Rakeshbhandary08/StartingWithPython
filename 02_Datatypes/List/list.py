numbers=[10,20,30,40,50,60]

print(numbers)
print(type(numbers))


#list can store another list -> Nested list
numbers=[10,20,30,40,50,[60,70]]
numbers.append(1000)
print(numbers)


#Insert element in a specific index
numbers.insert(0,1)
print(numbers)


fruits=['mongo','apple','guava']

numbers.extend(fruits)
print(numbers)


#Sorting
arr=[5,9,2,90,2,100,11,89,0,8]

#FInd the maximum value
maxVal=max(arr)
print(f"Maximum value of arr is {maxVal}")

print(f"Sum of all elements of arr is {sum(arr)}")


#Sort in ascending order
arr.sort()

#sort in descending order
arr.sort(reverse=True)
print(arr)

