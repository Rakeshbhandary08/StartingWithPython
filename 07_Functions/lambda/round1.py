#A lambda Function is a small anonymous function that can contain only one expression.

#FInd the square of a number
#lambda = argument:expression

square=lambda input:input*input

print(square(10))

#Check even or odd

check=lambda num:"Even" if num%2 == 0 else "Odd"

print(check(13)) #odd
print(check(200)) #even

#Find the maximum of two numbers

findMax=lambda a,b : a if a > b else b

print(findMax(100,800))