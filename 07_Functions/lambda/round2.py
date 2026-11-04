# Create a lambda function that:
# 1. Accepts three numbers: a, b, and c.
# 2. Returns their sum.
# 3. Returns the result when called with 10, 20, 30.

result=lambda a,b,c:a+b+c

print(result(10,20,30))


# Create a lambda function that accepts a number and returns:
# - "Positive" if the number is greater than 0.
# - "Negative" if the number is less than 0.
# - "Zero" if the number is 0.

# check=lambda num:"Positive" if num > 0 else "Negative" if num < 0 else "Zero"

# print(check(0))


# Create a lambda function that accepts two numbers and returns the larger number.

# But there's a twist:
# - If both numbers are equal, return "Both are equal".
# - Otherwise, return the larger number.


check=lambda a,b:a if a > b else "Both are equal" if a==b else b

print(check(10, 20))  # 20
print(check(50, 10))  # 50
print(check(5, 5))  # Both are equal


#Create a lambda function that accepts a string and returns its length.
strr=lambda string:len(string) if isinstance(string,str) else "Only Strings are allowed"

print(strr("Python"))
print(strr([1,2,3]))