#new_dict = {key_expression: value_expression for item in iterable}

#Create a square dictornary
numbers = [1, 2, 3, 4, 5]
square={num:num*num for num in numbers}
print(square)


#Convert two list into dictionary
names = ["Rakesh", "Rahul", "Aman"]
ages = [23, 24, 22]

users={names[i]:ages[i] for i in range(len(names))}

print(users)


students = {
    "Rakesh": 85,
    "Rahul": 32,
    "Aman": 76,
    "Rohit": 28
}

print({name:marks for name,marks in students.items() if marks >= 40})