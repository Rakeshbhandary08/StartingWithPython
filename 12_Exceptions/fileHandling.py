
# file=open('12_Exceptions/tryExcept.py','r');
# content=file.read()
# # print(content)

# with open('12_Exceptions/practice.txt','w') as file:
#     file.write("My self Rakesh Bhandary\n")
#     file.write("Write with the help of python built in method OPEN")
    

# try:   
#  with open("12_Exceptions/practice.text",'r') as file:
#     data=file.read()
#     print(data)
# except FileNotFoundError:
#   print("This file doesn't exist")

# print("File reading done")

#Raising Custom Exceptions

def set_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age shoule be between 1 to 120")
    print(f'Your age is {age}')

try:
 set_age(1000)
except ValueError as e:
   print("Error caught",e)

print("Done")
