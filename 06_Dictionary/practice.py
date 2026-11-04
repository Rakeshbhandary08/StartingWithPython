school_data = {
    "Aarav": {
        "Math": {"Term 1": 85, "Term 2": 90},
        "Science": {"Term 1": 78, "Term 2": 82},
        "English": {"Term 1": 88, "Term 2": 92}
    },
    "Diya": {
        "Math": {"Term 1": 92, "Term 2": 95},
        "Science": {"Term 1": 90, "Term 2": 88},
        "English": {"Term 1": 85, "Term 2": 89}
    },
    "Kabir": {
        "Math": {"Term 1": 65, "Term 2": 70},
        "Science": {"Term 1": 72, "Term 2": 75},
        "English": {"Term 1": 80, "Term 2": 78}
    }
}


#Calculate overall average marks for each student 
# (across all terms and subjects combined).

# Task 1: Har student ka overall average nikalne ka code
student_averages = {}

print(school_data.items());

for student, subjects in school_data.items():
    total_marks = 0
    total_terms = 0


    print("subjects",subjects)
    
    # Nested dictionaries me loop chalana
    for subject, terms in subjects.items():
        for term, marks in terms.items():
            total_marks += marks
            total_terms += 1
            
    # Average nikal kar round off karna
    avg = total_marks / total_terms
    student_averages[student] = round(avg, 2)

print(student_averages)