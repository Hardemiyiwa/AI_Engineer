# Student Score Tracker
# asking user for user for the student name and score
student_names = input("Enter 3 student name (seperated by space): ").split(" ")
student_score = []
for i in range(len(student_names)):
    score = int(input(f"Enter {student_names[i]} score: "))
    student_score.append(score)

students = {names: scores for names, scores in zip(student_names, student_score)}
# printing the output
print(f"\n\tName\t\tScore\n\t{student_names[0]}\t\t{student_score[1]}\n\t{student_names[1]}\t\t{student_score[0]}\n\t{student_names[-1]}\t\t{student_score[-1]}")
