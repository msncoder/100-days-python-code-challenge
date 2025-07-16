#Input a number and print whether it’s odd or even.

# inp = int(input("Enter a number")) 

# if inp % 2 == 0:
#     print("odd")
# else:
#     print("even")

# Positive, Negative or Zero
# Take a number from user and classify it.

# inp = int(input("Enter a number"))

# if inp < 0:
#     print(f"{inp} is negative number")
# elif inp == 0:
#     print(f"{inp} is a zero")
# else:
#     print("it's a positive number")


# Voting Eligibility Checker
# Input age and check if eligible to vote (age ≥ 18).

# age = int(input("Enter a your age"))

# if age >= 18:
#     print("you can vote")
# else:
#     print('you can not able vote')

# Max of 3 Numbers
# Input 3 numbers and print the greatest.

# num1 = int(input("Enter a first number"))
# num2 = int(input("Enter a second number"))
# num3 = int(input("Enter a third number"))

# if num1 >= num2 and num1 >= num3:
#     print("num1 is greatest")
# elif num2 >= num1 and num2 >= num3:
#     print("num2 is greatest")
# else:
#     print("num3 is greatest")


# Grade Calculator
# Input marks and print grade:
# >90: A
# 70–90: B
# 50–69: C
# <50: Fail


# english = int(input("Enter a English Marks"))
# maths = int(input("Enter a Math's Marks"))
# computer = int(input("Enter a computer's Marks"))

# total = english + maths + computer

# per = (total/300) * 100

# if per >= 90:
#     print("you have secured a+ grade")
# elif per >= 80 and per < 90:
#     print("you have secured a grade")
# elif per >= 70 and per < 80:
#     print("You have secured b grade")
# elif per >= 60 and per < 70:
#     print("You have secured c grade")
# elif per >= 50 and per < 60:
#     print("You have secured d grade")

# else:
#     print("Fail")


# Loops (for + while)
# Print Numbers from 1 to N using for loop
# (N is user input)

# inp = int(input("Enter a number want loop"))

# print("for loop")
# for i in range(inp):
#     print(i)

# print("While loop")

# a = 0
# while (a < inp):
#     print(a)
#     a+=1


# Sum of First N Natural Numbers
# Use both for and while loop approaches.

# inp = int(input("Enter a number"))
# sum = 0

# for i in range(1,inp+1):
#     sum += i
# print(sum)


# Factorial of a Number (n!)

# inp = int(input("enter a number"))
# fact = 1

# for i in range(1,inp+1):
#     fact*=i

# print(fact)


# Reverse a Number
# Input: 123 → Output: 321

# inp = int(input("Enter a three digit"))

# a = inp % 10
# b = inp // 10
# # print(a)
# # print(b)
# c = b % 10
# # print(c)
# d = b // 10
# # print(d)
# rev = f"{a}{c}{d}"
# print(int(rev))

# Check if a Number is Prime

inp = int(input("Enter a number"))

if inp <= 1:
    print("not a prime number")
else:
    for i in range(2, inp):
        if (inp % i) == 0:
            print("not a prime number")
            break
    else:
        print("its a prime number")