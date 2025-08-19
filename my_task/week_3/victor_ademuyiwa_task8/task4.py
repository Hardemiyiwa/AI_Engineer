# Student Record
student = {}

# Collecting user details
name = input("Enter your name: ")
age = int(input("Enter your age: "))

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
passed = (average_score > 50)
student["passed"] = passed

# checking if the student is a teenager
teenager = student["age"] >= 13 and student["age"] <= 19

print(f"\nStudent Record:\nName: {student["name"]}\nAge: {student["age"]}\nScores: {student["scores"]}\nPassed: {student["passed"]}\nTeenager: {teenager}")
