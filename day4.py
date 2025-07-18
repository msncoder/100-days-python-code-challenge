# Take user input (name) and greet them:

# Input: Ali → Output: Hello, Ali!

# name = input("Enter a name")
# print(f"Hello, {name}!")


# Check if a string contains a certain word:

# Input: "I love Python"

# Search: "Python" → Output: Found

# INP = input("Enter a word")
# search = "python"

# if "python" in INP:
#     print("Found")
# else:
#     print("Not Found")


# Count vowels in a string.
# Input: "hello" → Output: 2

# inp = "hello"
# vowels = "aeiouAEIOU"
# count = 0

# for i in range(len(inp)):
#     # print(inp[i])
#     if inp[i] in vowels:
#         count+=1

# print(count)


# Convert "python programming" to "Python Programming" using .title().

# word = "python programming"
# s=word.title()
# print(s)


# Find how many times a word appears:

# Input: "I love python because python is awesome"

# Word: "python" → Output: 2

# inp = input("Enter a sentence")
# inpspl = inp.split(" ")
# # print(inpspl)

# count = 0
# word = "python"

# for i in range(len(inpspl)):
#     # print(inpspl[i])
#     if word == inpspl[i]:
#         count+=1
# print(count)



# Check if a string is a palindrome (same forward and backward)
# Input: "madam" → Output: Yes
# Hint: string == string[::-1]

# inp = input("Enter a word")
# if inp == inp[::-1]:
#     print("it's a palindrom")
# else:
#     print("it's not a palindrom")


# Reverse each word in a sentence:
# Input: "hello world" → Output: "olleh dlrow"

# inp = input("Enter a sentence")
# spl = inp.split(" ")
# rev = ""

# print(len(spl))
# for i in range(len(spl)-1,-1,-1):
#     print(spl[i])


# Remove all spaces from a sentence.
# sentence = input("Enter a sentence").split(" ")
# without_space = ""
# for i in range(len(sentence)):
#     # print(sentence[i])

#     without_space += sentence[i]

# print(without_space)


# Count uppercase and lowercase letters in a string.

# string = input("Enter a word")
# count_upper = 0
# count_lower = 0

# for i in range(len(string)):
#     if string[i] == string[i].lower():
#         count_lower += 1
#     else:
#         count_upper += 1

# print(count_upper)
# print(count_lower)


# Accept full name, split into first name and last name:

# Input: "Muhammad Saad" → Output: First: Muhammad, Last: Saad

name = input("Enter Your name")
name = name.split(" ")
print(f"Your First name is {name[0]}")
print(f"Your Last name is {name[1]}")