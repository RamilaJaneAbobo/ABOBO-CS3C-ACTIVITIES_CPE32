'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#1).  Python program to create an array of 3 integers and display the array items.
a = [1,3,5]
print(a[0])
print(a[1])
print(a[2])
print("")

#2). Python program to append a new item to the end of the array.
import array
original_array = array.array('i', [1, 3, 5, 7, 9])
print("Original array:", original_array)

original_array.append(11)

print("New array:", original_array)
print("")

#3). Python program to reverse the order of the items in the array.
original_array = array.array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array:", original_array)

original_array.reverse()

print("New array:", original_array)
print("")

#4.) Python program to find out if a given array of integers contains any duplicate elements.
def contains_duplicates(arr):
    return len(arr) != len(set(arr))

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 3, 4, 5]
arr3 = [1, 2, 3, 1, 4, 5]

print(contains_duplicates(arr1))
print(contains_duplicates(arr2))  
print(contains_duplicates(arr3)) 
print("")

#5.)  Python program to find the first duplicate element in a given array of integers. 
def first_duplicate(arr):
    seen = set()
    
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    
    return -1

arr1 = [1, 2, 3, 4, 5, 4]
arr2 = [1, 2, 3, 4, 5]
arr3 = [1, 1, 2, 3, 4, 5]

print(first_duplicate(arr1))  
print(first_duplicate(arr2))  
print(first_duplicate(arr3))  




