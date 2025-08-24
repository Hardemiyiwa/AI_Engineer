# Student Score Tracker
# asking user for user for the student name and score
student_names = []
while len(student_names) != 3:
    student_names = input("Enter 3 student name (seperated by space): ").split(" ")
    if len(student_names) != 3:
        print(f"invalid {student_names}")
student_score = []
for i in range(len(student_names)):
    score = int(input(f"Enter {student_names[i]} score: "))
    student_score.append(score)
students = {names: scores for names, scores in zip(student_names, student_score)}
# printing the student name and score
print(students)
for name, score in students.items():
    print(f"{name} score is {score}")
