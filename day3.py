# Input 5 numbers from user and store in list, then:
# Print sum, max, and min.
# a = []
# for i in range(5):
#     inp = int(input("Enter a number"))
#     a.append(inp)
# # print(a)

# sum = 0

# for i in range(0,len(a)):
#     # print(a[i])
#     sum+=a[i]

# print(f"sum of inp number is {sum}")

# max = a[0]
# for i in range(0,len(a)):
#     if a[i] > max:
#         max = a[i]

# print(f"maximum number in list is {max}")

# min = a[0]
# for i in range(0,len(a)):
#     if a[i] < min:
#         min = a[i]

# print(f"minimum number in list is {min}")


# Reverse a list using slicing and loop.

# li = [111,2,3,4,5,666]
# rev = []



# for i in range(len(li)-1,-1,-1):
#     # print(li[i])
#     rev.append(li[i])

# print(rev)
    

# Remove all even numbers from a list.

# li = [1,2,3,4,5,6]
# result = []
# for i in range(len(li)):
#     if li[i] % 2 != 0:
#         result.append(li[i])
# print(result)


# Count frequency of each element in a list:
# Input: [1, 2, 2, 3, 3, 3] → Output: {1:1, 2:2, 3:3}

# Input = [1, 2, 2, 3, 3, 3]
# output = {}
# for i in range(len(Input)):
#     # print(Input[i])
#     if Input[i] not in output:
#         output[Input[i]] = 1
#     else:
#         output[Input[i]] += 1

# print(output)


# Find second largest number in a list.
# a = [1,2,3,4,5]
# largest = a[0]
# second_largest = a[1]

# for i in range(len(a)):
#     # print(a[i])
#     if a[i] > largest:
#         second_largest = largest
#         largest = a[i]

# print(largest)
# print(second_largest)



# Create a tuple with numbers and:

# Count occurrences of a number.

# Find index of a number.

# tup = (1,2,3,5,4)
# count = {}

# for i in range(len(tup)):
#     if tup[i] not in count:
#         count[tup[i]] = 1
#     else:
#         count[tup[i]] += 1

# print(count)


# Write a function that accepts a tuple of numbers and returns a new tuple with only even numbers.


# tup = (1,2,3,4,5,6)
# even_tuple = []

# for i in range(len(tup)):
#     print(tup[i])
#     if tup[i] % 2 == 0:
#         even_tuple.append(tup[i])

# print(tuple(even_tuple))


# Input name and age of 3 students and store in a tuple list like:
# [("Ali", 20), ("Sara", 22), ("Hamza", 21)]

# name_and_age = []

# for i in range(3):
#     name = input("Enter a name ")
#     age = int(input("Enter a age "))

#     a = (name,age)
#     name_and_age.append(a)

# print(name_and_age)



# Union

# Intersection

# Difference (A - B)

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# c = A.union(B)
# print(c)
# d = A.intersection(B)
# print(d)
# f = A.difference(B)
# print(f)

# From a list with duplicates, convert to set to remove duplicates.
# li = [1,1,2,2,3,4,4,3,5,6,5,4]
# remove_dublicate = set(li)
# print(remove_dublicate)