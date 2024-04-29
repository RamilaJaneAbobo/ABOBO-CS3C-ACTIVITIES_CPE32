'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#Python function to find the maximum of three numbers
def find_max(num1, num2, num3):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    return max_num

num1 = 50
num2 = 30
num3 = -25
print("Maximum of", num1, ",", num2, "and", num3, "is:", find_max(num1, num2, num3))
print("")

# Python function to sum all the numbers in a list
def sum_number(numbers):
    total = 0
    for num_bers in numbers:
        total += num_bers
    return total

num_list = [60, 20, 10, 80, 50]
print("Sum of numbers in the list:", sum_number(num_list))
print("")

#Python program to reverse a string
def reverse_string(input_string):
   
    return input_string[::-1]

# Example usage:
original_string = "Hello,  Welcome!"
reversed_string = reverse_string(original_string)
print("Original String:", original_string)
print("Reversed String:", reversed_string)
print("")

#Python function that accepts a string and counts the number of upper and lower case letters
def count_upper_lower(string):
 
    upper_count = 0
    lower_count = 0

    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

input_string = "Hello Welcome! Thank you for coming!"
upper_count, lower_count = count_upper_lower(input_string)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)
print("")

#Python function that takes a list and returns a new 
#list with distinct elements from the first list
def get_unique_elements(input_list):
   
    return list(set(input_list))

original_list = [1, 3, 2, 6, 4, 7, 5]
unique_list = get_unique_elements(original_list)
print("Original List:", original_list)
print("List with Distinct Elements:", unique_list)






