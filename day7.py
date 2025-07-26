# Create a dictionary of 5 students with names as keys and marks as values

# dic = {"Ali": 87, "Sara": 92,"bilal":99,"samad":85,"fahad":55}

# # print(dic.keys())
# # print(f"{dic.keys()} has got {dic.values()} Marks")

# for i in dic.items():
#     print(f"{i[0]} has got {i[1]} Marks")

# Take a name input from user and check if student exists
# → if yes, print marks.

# name = input("Enter a Name")
# dic = {"Ali": 87, "Sara": 92,"bilal":99,"samad":85,"fahad":55}


# if name in dic.keys():
#     print("Yes")
# else:
#     print("No")


# Find the student with highest marks

# dic = {"Ali": 87, "Sara": 92,"bilal":99,"samad":85,"fahad":55}
# student_name = ''
# highest_marks = -1

# for name,marks in dic.items():
#     if marks > highest_marks:
#         highest_marks = marks
#         student_name = name

# print(f"The name of student is {student_name} has highest marks {highest_marks}")


# Count frequency of characters in a string using dict

# Input: "banana" → Output: {'b': 1, 'a': 3, 'n': 2}

# inp = input("Enter a word")
# count = {}

# for i in inp:
#     if i in count:
#         count[i] += 1
#     else:
#         count[i] = 1
# print(count)

# Convert this dictionary to a JSON string and print:

import json

# data = {
#     "name":"saad",
#     "age":15,
#     "skills":["Python","Django"]
# }

# json_string = json.dumps(data,indent=1)
# print(type(json_string)) 


# data = {
#     "name": "Saad",
#     "age": 15,
#     "skills": ["Python", "Django"]
# }

# with open("data.json","w") as f:
#     json.dump(data,f,indent=4)


# Load the file and print content

# with open("data.json","r") as f:
#     loaded_data = json.load(f)
#     print(loaded_data)


# Write user input to notes.txt

# inp = input("Enter a note")

# with open("notes.txt",'w') as f:
#     f.write(inp)


# with open('notes.txt','r') as f:
#     content = f.read()
#     print(content)

