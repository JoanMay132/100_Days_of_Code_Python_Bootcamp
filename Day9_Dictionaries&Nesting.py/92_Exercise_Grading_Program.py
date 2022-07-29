student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades={}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score=student_scores[student]
    if score>=91:
        student_grades[student]="Outstanding"
    elif score>=81:
        student_grades[student]="Exceeds Expectations"
    elif score>=71:
        student_grades[student]="Acceptable"
    else:
        student_grades[student]="Fail"
#student_grades["Harry"]="Exceeds Expectations"
#student_grades["Ron"]="Acceptable"
#student_grades["Hermione"]="Outstanding"
#student_grades["Draco"]="Acceptable"
#student_grades["Neville"]="Fail"
    

# 🚨 Don't change the code below 👇
print(student_grades)   