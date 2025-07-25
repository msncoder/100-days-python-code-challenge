# Simple greeting function
# Input: "Ali" → Output: "Hello Ali!"

# def NamePrint(name):
#     print(f"Hello {name}")

# NamePrint("saad")


# Function to calculate square & cube

# square(n) → n * n

# cube(n) → n * n * n

# def sqaure(n):
#     print(n*n)

# sqaure(3)

# def cube(n):
#     print(n*n*n)

# cube(3)

# Check even or odd using function 

# def even_odd(n):
#     if n % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")


# even_odd(2)


# Function that takes a list and returns the sum of elements

# li = [1,2,3,4,50]

# def sum_of_li(li):
#     sum = 0
#     for i in li:
#         # print(li[i])
#         sum+=i
#     return sum

# print(sum_of_li(li))


# Function to return factorial of a number (non-recursive)


# def factorial_num(num):
#     fact = 1
#     for i in range(num):
#         a = i+1
#         fact *= a 
#     return fact

# print(factorial_num(4))


# Use *args to sum any number of inputs
# Example: sum_all(2, 4, 5, 6)


# def sum_of_args(*args):
#     # print(args)
#     sm = 0
#     for i in args:
#         # print(i)
#         sm+=i
#     return sm

# print(sum_of_args(1,2,3,4))


# Function with default argument

# greet(name="Guest") → Output: "Hello Guest"


# def default_args_function(name="Guest"):
#     print(f"Hello {name}")

# default_args_function()

# Function to count vowels in a string

# def count_vowels(word):
#     count = 0
#     vowels = 'aeiouAEIOU'

#     for i in word:
#         if i in vowels:
#             count += 1
        
#     return count

# print(count_vowels("saad"))


# Use *args to sum any number of inputs
# Example: sum_all(2, 4, 5, 6)

# Use **kwargs to display student data
# Example: student(name="Ali", age=15, class="10th")

# def kwargs_function(**kwargs):
#     print(kwargs)

# kwargs_function(name="saad", age=15, clas="10th")


#  Factorial using recursion

# def Recurion_Fact(n):
#     if n == 0 or n == 1:
#         return 1

#     return n * Recurion_Fact(n-1)

# print(Recurion_Fact(8))


# Recursive Function for Fibonacci (Simple Version)

# def fibonacci(n):
#     if n == 1 or n == 0:
#         return 1
    
#     return fibonacci(n-1) + fibonacci(n-2)

# for i in range(10):
#     print(fibonacci(i), end=" ")