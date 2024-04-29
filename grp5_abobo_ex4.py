'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
score = float(input("\n Kindly Enter the student's score here: "))                              

if score > 90:
    grade = 'A (PASSED)'
elif score > 75:
    grade = 'B (PASSED)'
elif score > 65:
    grade = 'C (FAILED'
else:
    grade = 'D (FAILED)'

print("\n The student's  grade is:", grade)