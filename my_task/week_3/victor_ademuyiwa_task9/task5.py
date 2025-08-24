#  Unique Name
# creating an empty set
seminal_attendance = set()

# Adding the collected to the set
while True:
    attendance = input("Enter your name (Enter done when there is no member left): ")
    if attendance.lower().strip() == "done":
        break
    elif attendance in seminal_attendance:
        print(f"{attendance} already in attendance")
    else:
        seminal_attendance.add(attendance)

# displaying the name in alphabetical order
print(f"{", ".join(sorted(seminal_attendance))}")