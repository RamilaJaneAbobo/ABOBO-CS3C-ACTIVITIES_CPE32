'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#1. Python program find difference between each number in the array and the average of all numbers

def find_difference(arr):
    if not arr:
        return []

    avg = sum(arr) / len(arr)

    differences = [num - avg for num in arr]

    return differences

numbers = [2, 3, 4, 5, 6]
result = find_difference(numbers)
print(result)
print("")
#2. Python program to convert a string in an array

def string_to_array(input_string):
    return list(input_string)

input_str = "Hello, Welcome!"
result_array = string_to_array(input_str)
print(result_array)
print("")

#3. Python program to convert a string in an arrays

def split_even_odd(arr):
    even_numbers = [num for num in arr if num % 2 == 0]
    odd_numbers = [num for num in arr if num % 2 != 0]

    return even_numbers, odd_numbers

numbers = [1, 12, 3, 45, 50, 6, 17, 8, 29]
even, odd = split_even_odd(numbers)
print("Even numbers:", even)
print("Odd numbers:", odd)
print("")

#4. Python program to convert a string in an array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

numbers = [99, 81, 20, 46, 13]
insertion_sort(numbers)
print("Sorted array:", numbers)