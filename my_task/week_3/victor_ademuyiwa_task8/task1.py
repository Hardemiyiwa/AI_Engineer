# Collecting user input (collecting integer numbers)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Checking if num1 is  eaqual to num2
print(f"{num1} == {num2} : {num1 == num2}") 
# Output: 3 == 7 : False the result is false  because the num1 value which is eaqual to three is lesser than num2 value which is equal to seven

# checking if num1 is not equal to num2
print(f"{num1} != {num2} : {num1 != num2}")
# Output: 3 != 7 : True the result is true because the num1 value which is equal to three is lesser than the num2 value which is equal to seven

# Checking if num1 greater than num2
print(f"{num1} > {num2} : {num1 > num2}") 
# Output: 3 > 7 : True the result is false because the num1 value which is equal to three is lesser than the num2 value which is equal to seven

# Checking if num1 less than num2
print(f"{num1} > {num2} : {num1 > num2}") 
# Output: 3 > 7 : True the result is true because the num1 value which is equal to three is lesser than the num2 value which is equal to seven

# Give 3 usecases or cenarios where you can apply program
"""
1. Human growth stages in life (teenage and  adult)
2. Admissions eligibility check
3. Autheticating the age limit of people that can enter club party
"""
# Autheticating the age limit of people tha can enter club party
# collecting user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
# checking if the user is 18 years or above
eligibility = age >= 18
print(f"Candidate: {eligibility}")

# giving the user the years they can come back to participate
