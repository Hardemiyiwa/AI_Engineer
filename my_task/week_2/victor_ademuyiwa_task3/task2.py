# Check if a given string contain python
text = "Are you learning python"
print("python" in text)

# Reverse a string without using slicing ([::-1])
text = "Python"
print("".join(reversed(text)))

# string with extra spaces, removing the leading and the trailing space
text = "  NCC  "
print(text.strip())

# user to enter a sentence and print the number of vowels in it
user = input("Write a sentence: ").lower()
count  = user.count("a") + user.count("e") + user.count("i") + user.count("o") + user.count("u")
print(f"Total vowel: {count}")

# convert a string "1234" to an integer and multiply it by 2.
text = int("1234")
print(text * 2)

