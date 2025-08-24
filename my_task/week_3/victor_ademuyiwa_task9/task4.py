# admission
# applicant details
name = input("Enter your name: ").title()
age = int(input("Enter your age: "))
first_chioce = input("Do you choose UNILAG as your first choice\nYes or No: ").lower()
post_utme = input("Do you participate in the university's online Post-UTME Screening\nYes or No: ")
jamb_score = int(input("Enter your jamb score: "))

# collecting subjects names
subjects_unique = {"Mathematics", "English"}
print("five(5) credit passes at one sitting in relevant O'Level subjects, including English Language and Mathematics\n1. English\n2. Mathematics\nEnter the reminging three(3)")
count = 3
while count <= 5:
    subject = input(f"{count}: ").title()
    if subject in subjects_unique:
        print("Subject already exist")
    else:
        subjects_unique.add(subject)
        count += 1
subject_list = list(subjects_unique)

# collecting each subject grade
subject_grade = []
for subj in subject_list:
    grade = input(f"Enter your grade in {subj}: ").upper()
    subject_grade.append(grade)

# storing the subjects and grades in a dictionary
subjects_grades = {names: grades for names, grades in zip(subjects_unique, subject_grade)}
print(subjects_grades)

# Checking for participant eligibility
if age >= 16 and first_chioce == "yes" and post_utme == "yes" and jamb_score >= 200:
    # Checking grade eligibility (grade = A, B or C)
    for key in subjects_grades:
        result = subjects_grades[key] == "A" or subjects_grades[key] == "B" or subjects_grades[key] == "C"
        if result == False:
            break
    print(result)
    if result == True:
        print("\n\"\"\"\nCongratulations!🎉 You have been successfully admitted in to our\ninstitution. We are excited to welcome you and look forward to\nsupporting your academic and personal growth.\n\"\"\"")
    else:
        print("\n\"\"\"\nWe appreciate your intrest in our institution. Unfortunately, you where\nnot offered admission this session. We encourage you to keep striving\nreapply, and wish you success in your future endeavors.\n\"\"\"")
else:
    print("\n\"\"\"\nWe appreciate your intrest in our institution. Unfortunately, you where\nnot offered admission this session. We encourage you to keep striving\nreapply, and wish you success in your future endeavors.\n\"\"\"")
