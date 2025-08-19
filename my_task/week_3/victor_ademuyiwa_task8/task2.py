# # collecting user details (name, age, score)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# score = int(input("Enter your test score: "))

# # checking if the student is qualify or not
# eligibility = (age <  18) and  (score > 70)
# print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")
"""
The code above is to check is a candidate is qualify for a program or not
First step: the user details was collected
second step: we check if the candidate score is greater than 70 and if the candidate is below 18 years old. then if the canditate meet the requirement, the eligibility will be true while if it doesn't the eligibility will be fasle
"""

# Federal Government Scholarship key Eligibility Requirements
# Collecting user details
name = input("\nEnter your name: ")
age = int(input("Enter your age: "))
nationality = input("Enter your nationality: ").title()
enrollment = input("Are you a full-time undergraduate in a recognized Nigerian University ?\nEnter (yes/no): ").lower()
other_scholarhips = input("Are you currently receving any other scholarship from an entity in the Oil and Gas industry, whether national or internation ?\nEnter (yes/no): ").lower()

# Academic qualification
english = input("Enter your English grade (A, B, C, D, E or F) in your WAEC/WASSCE(May/June) exams: ").upper()
mathematics = input("Enter your Mathematics grade (A, B, C, D, E or F) in your WAEC/WASSCE(May/June) exams: ").upper()
other_subject = input("Do you have \"As\" or \"Bs\" in other three relevant subject in your WAEC/WASSCE(May/June) exams\nEnter (yes/no): ").lower()

academic_qualification = (english == "A" or english == "B") and (mathematics == "A" or mathematics == "B") and (other_subject == 'yes')

# Checkng for user eligibility
eligibility = (nationality == "Nigeria") and (enrollment == "yes") and (other_scholarhips == "no") and (academic_qualification == True)

print(f"\nFederal Government Scharship Eligibility Status\nCandidate Name:\t\t\t\t{name}\nAge:\t\t\t\t\t{age}\nNationality:\t\t\t\t{nationality}\nFull-time in NG reg. sch.:\t\t{enrollment}\nOn ther scholarship (Oil and Gas):\t{other_scholarhips}\nAcademic Requirement:\t\t\t{academic_qualification}\nEligible:\t\t\t\t{eligibility}")