# Filter Even Numbers from List

# Input: [1, 2, 3, 4, 5] → Output: [2, 4]


# inp = [1, 2, 3, 4, 5]
# even_li = []
# for i in inp:
#     if i % 2 == 0:
#         even_li.append(i)

# print(even_li)


# Count Positive, Negative, and Zeroes in a list.
# Positive_count = 0
# Negative_count = 0
# zeros_count = 0

# li = [1,1,2,3,0,0,-2,-3,-4]

# for i in li:
#     if i > 0:
#         Positive_count += 1
#     elif i < 0:
#         Negative_count += 1
#     else:
#         zeros_count += 1

# print(Positive_count)
# print(Negative_count)
# print(zeros_count)



# Find Maximum and Minimum Number in a List (without using max()/min()).

# li = [5,4,3,2,1]
# min_num = li[0]
# max_num = li[0]

# for i in li:
#     if max_num < i :
#         max_num = i

#     if min_num > i:
#         min_num = i

# print(min_num)
# print(max_num)


# Search for an element in a list → return index if found, else "Not Found".

# li = [1,2,3,4,5,6,7]

# inp = 4

# def search(li,inp):
#     if inp in li:
#         return f" Element {inp} found at index {li.index(inp)}"
#     else:
#         return "Not Found"

# print(search(li,inp))


# Remove Duplicates from List using:
# set
# custom loop logic

# li = [1,1,2,2,3,3,4]

# # dub_remove = set(li)

# # print(dub_remove)

# dub_remove = []

# for i in li:
#     if i not in dub_remove:
#         dub_remove.append(i)

# print(dub_remove)


# Create a function that takes a list and returns the reversed list

# li = [1,2,3,4,5]
# def reverse_li(li):
#     rev_li = []
#     for i in range(len(li)-1,-1,-1):
#         rev_li.append(li[i])
#     return rev_li


# print(reverse_li(li))

# Write a function to calculate average of list elements

# li = [1,2,3,4,5]

# def avg_li(li):
#     sum = 0
#     for i in li:
#         sum += i
#     return sum / len(li)

# print(avg_li(li)) 


# Function to find second largest element in list
li = [0,6,4,5]
def second_larg(li):
    largest = float('-inf')
    second_largest = float('-inf')
    for i in li:
        if i > largest:
            second_largest = largest
            largest = i
            # print("if")
            
        elif i > second_largest and i != largest:
            second_largest = i
            # print("elif")
    return largest,second_largest
        

print(second_larg(li))

