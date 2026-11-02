str="Rakesh Kumar Bhandary";

print(type(str))

print(str)

#Print first name ,middle name and last name individually

first_Name=str[0:6]
middle_name=str[7:12]
print(f"First Name is {first_Name}")
print(f"Middle Name is {middle_name}")
print(f"Last Name is {str[13:]}")