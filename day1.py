# Take name & age as input and print in this format: Hi Ali, you are 15 years old!

# name = input("Enter a name Please")
# age = input("Enter a age Please")

# print(f"Hi {name}, You are {age} year old!")


# Convert Fahrenheit to Celsius.

# degree = int(input("Enter a degree in fahrenheite"))

# c = round((degree - 32) * 5/9)

# print(f"Faherheit {degree} ==== Celsius {c}")


# Swap two variables without using a third variable.

# a = 10
# b = 11
# temp = None

# temp = a
# a = b
# b = temp

# print(a)
# print(b)


# Calculate area and perimeter of a rectangle

# a  = l * w 
# P=2(l+w)

# lenght = int(input("Enter a length of rectangle"))
# width = int(input("Enter a width of rectangle"))

# area = lenght * width

# perimeter = 2*(lenght+width)

# print(f"The area of Reactangle is {area} and The Perimeter of Reactangle is {perimeter}")


# Take 3 inputs: marks in 3 subjects → find average and percentage.

# english = int(input("Enter a English Marks"))
# computer = int(input("Enter a computer Marks"))
# Maths = int(input("Enter a Math's Marks"))

# total = english + computer + Maths

# per = (total / 300 ) * 100

# print(f"The Percentage is {round(per,3)}")


# Take a string and reverse it.

# str = input("Enter a string")
# rev = ""

# for i in range(len(str)-1,-1,-1):
#     # print(str[i])
#     # print(i)
#     rev += str[i]

# print(rev)


# Count vowels in a string.

# str = input("Enter a word")
# vowels = 'aeiouAEIOU'
# count = 0

# for i in range(len(str)):
#     # print(i)
#     if str[i] in vowels:
#         count += 1

# print(count)


# Check if a number is even or odd.

# num = int(input("Enter a Number"))

# if num % 2 == 0:
#     print(f"{num} is even")
# else:
#     print(f"{num} is odd")


# Check if input is an integer or string.
# inp = input("Enter an input: ")

# try:
#     int(inp)
#     print("Number")
# except ValueError:
#     print("String")



# Take a number and print its multiplication table.

# num = int(input("Enter a number"))

# for i in range(1,11):
#     print(f"{num} * {i} = {num*i}")