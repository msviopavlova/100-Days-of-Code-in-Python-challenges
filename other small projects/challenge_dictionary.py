student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


student_grades = {}
for key_name in student_scores:
    old_score = student_scores[key_name]
    new_grade = ""
    if 91 <= old_score <= 100:
        new_grade = "Outstanding"
    elif 81 <= old_score <= 90:
        new_grade = "Exceeds Expectations"
    elif 71 <= old_score <= 80:
        new_grade = "Acceptable"
    elif old_score <= 70:
        new_grade = "Fail"
    student_grades[key_name] = new_grade



print(student_grades)





