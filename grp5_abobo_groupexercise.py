'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

#Display numbers from -10 to -1 using for loop
for num in range(-10, 0):
    print(num)
    print("")
  
#Use else block to display a message “Done” after successful execution of for loop
for num in range(-10, 0):
    print(num)
else:
    print("Done")
    print("")
    
#Write a program to display all prime numbers within a range
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print(f"Prime numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
            print("")
            
#Use a loop to display elements from a given list present at odd index positions
given_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print("Elements at odd index positions:")
for i in range(1, len(given_list), 2):
    print(given_list[i])
    print("")

#Display numbers from a list using loop    
numbers = [12, 75, 150, 180, 145, 525, 50]

print("Numbers divisible by five:")
for num in numbers:
    if num % 5 == 0:
        if num > 500:
            print("Number greater than 500 encountered. Stopping loop.")
            break
        elif num > 150:
            print("Number greater than 150 encountered. Skipping.")
            continue
        else:
            print(num)  
    
    
