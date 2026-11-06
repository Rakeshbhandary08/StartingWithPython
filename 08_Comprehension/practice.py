students = {
    "Rakesh": [85, 90, 78],
    "Rahul": [35, 40, 32],
    "Aman": [90, 95, 88],
    "Rohit": [55, 60, 45],
    "Priya": [95, 92, 98]
}

#Create a new dictionary called total_marks that stores each student's total marks.
# total_marks={student:sum(marks) for student,marks in students.items() }
# print(total_marks)

total_subject=3
averages={name:round(sum(marks)/len(marks),2) for name,marks in students.items()}
print(averages)


# Now create a dictionary called passed.
# Condition: Students with an average of at least 40 are considered passed.

passed={name:average for name,average in averages.items() if average >= 40}
print(passed)

failed={name:average for name,average in averages.items() if average < 40}
print(failed)

# Using your existing averages dictionary, find:
# 1. The student's name who has the highest average.
# 2. Their average marks.

# topper={value for value in averages.values()}
# topperList=list(topper)

# answer={name:value for name,value in averages.items() if value == max(topperList)}
# print("Here is our topper",answer)

#Simple
topper=max(averages,key=averages.get)
print(topper,averages[topper])

