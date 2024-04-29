'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
#NUMBER FUNCTIONS
#abs() function
positive_num = 10
value_num = abs(positive_num)
print(" Value Number: ", value_num)

#int() function
num_str = "100"
num_int = int(num_str)
print(" Integer:", num_int)

#min() function
numbers = [3, 9, 10, 15]
min_value = min(numbers)
print(" Minimum value:", min_value)
print(" ")

#POWER AND lOGARITHMIC FUNCTIONS
#exponentiation operator
base = 3
exponent = 3
print( "", base ** exponent)  

#logarithm base 10
import math

x = 100
result = math.log10(x)
print("", result) 

#natural algorithm
x = 10
result = math.log(x)
print("", result)
print("")

#TRIGONOMETRIC FUNCTIONS
import math

angle = math.radians(40)  # Convert degrees to radians
print(" Sine:", math.sin(angle)) 
print(" Cosine:", math.cos(angle))  
print(" Tangen:", math.tan(angle)) 
print("")

#ANGULAR CONVERSION FUNCTIONS
import math

# Convert degrees to radians
angle_degrees = 45
angle_radians = math.radians(angle_degrees)
print(" degrees in radians:", angle_radians) 

# Convert radians to degrees
angle_radians = math.pi / 4
angle_degrees = math.degrees(angle_radians)
print(" radians in degrees:", angle_degrees)
print("")

#HYPERBOLIC FUNCTIONS
import math

# Hyperbolic functions
x = 2
print(" sine of 2:", math.sinh(x))  
print(" cosine of 2:", math.cosh(x)) 
print(" tangent of 2:", math.tanh(x))  
print(" acosh of 2:", math.tanh(x))  
print(" asinh of 2:", math.tanh(x))  

