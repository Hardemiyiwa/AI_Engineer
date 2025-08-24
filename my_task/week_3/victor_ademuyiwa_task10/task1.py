# Student Record
student = {}

# Collecting user details
name = input("Enter your name: ")
while True:
    try:
        age = int(input("Enter your age: "))
        break
    except ValueError as e:
        print(f"Error:", e)

# storing the details in a dictionary
student.update({
    "name": name,
    "age": age
})
print(student)

# Adding score to the list
student["scores"] = [70, 85, 90]

# checking if the student pass
average_score = sum(student["scores"]) / len(student["scores"])
print(average_score) 
if average_score > 50:
    student["Result"] = "Pass"
else:
    student["Result"] = "Fail"


# checking if the student is a teenager
if student["age"] >= 13 and student["age"] <= 19:
    student["Teenager"] = "Yes"
else:
    student["Teenager"] = "No"

print(f"\nStudent Record:\nName: {student["name"]}\nAge: {student["age"]}\nScores: {student["scores"]}\nResult: {student["Result"]}\nTeenager: {student["Teenager"]}")
