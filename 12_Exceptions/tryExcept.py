# # student={"name":"Rakesh","year":2027}

# # try:
# #  print(student["course"]) #sensitive call
# # except KeyError:
# #  print("Key is missing")

# # print("Hello world")

# def calling(a):

#     try:
#         if a=="unknown":
#          raise NameError("This is not valid value")
#     except NameError as e:
#         print("Error",e)
#     else:
#         print(f"This is {a}")
#     finally:
#         print("Function Execution is done")

# calling("unknown")

#Question 
# Task: Build a division calculator.

# Requirements:#
# 1. Take two numbers from the user.
# 2. Convert both inputs into integers.
# 3. Divide the first number by the second.
# 4. Handle division by zero.
# 5. Handle invalid input (for example, entering "hello" instead of a number).
# 6. Display "Program finished" regardless of whether an exception occurs.
# Constraints:
# - Use try and except.
# - Use separate except blocks for ZeroDivisionError and ValueError.
#- Don't use if/else to handle these errors.

# print("Welcome to Division Calculator")
# input("Write 2 values :")

def divisionCal(a,b):
     
     try:
          a=int(a)
          b=int(b)
          return round(a/b,2)
     except ZeroDivisionError:
          print("You can't perform this action")
     except ValueError:
          print("Values should be Number")
     finally:
          print("Program finished")


print(divisionCal(10,0))
print(divisionCal("Hello",10))
    