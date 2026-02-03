# ==========================================
# 1. Python Program Structure
# ==========================================
# Python executes code Top-Bottom
# No main() required

# Syntax : print("Your statement")
print("Hello World!!!")
print("This is a print function used to print statements in Python")


# ==========================================
# 2. Print and Input
# ==========================================
"""
print() - Output function
input() - Input function
"""

# Ex 1: Take input from user and display it
name = input("Enter your name: ")
print(f"Welcome {name}, in this section we are going to learn Fundamentals of Python!!")


# ==========================================
# 3. Variables & Datatype
# ==========================================
# Variable Stores Data Eg: a = 5 (5 is stored in "a")

# Different Types of datatype:
# int   -> Stores Integer values (5, 6, 7)
# float -> Stores Decimal Values (3.14, 10.5)
# bool  -> Stores Boolean Values (True / False)
# str   -> Stores string values ("world", "name")

# Ex 2: Showing details of student using different Data Types
age = 20
print(f"{age} and its Datatype :{type(age)}")

price = 99.5
print(f"{price} and its Datatype :{type(price)}")

student_name = "Nihal"
print(f"{student_name} and its Datatype :{type(student_name)}")

is_student = True
print(f"{is_student} and its Datatype :{type(is_student)}")


# ==========================================
# 4. Type Casting
# ==========================================
# Converting one Datatype to another (e.g., string to int)

# Ex 3: Example for Type casting
num1 = "1000"
num2 = "14.67"
print(f"Original types: {type(num1)}, {type(num2)}")

num_1 = int(num1)
num_2 = float(num2)
print(f"Converted types: {type(num_1)}, {type(num_2)}")


# ==========================================
# 5. Operators
# ==========================================
print("\n--- Arithmetic operators ---")
a = 10
b = 5
print(f"Addition : {a+b}")
print(f"Subtraction : {a-b}")
print(f"Multiplication : {a*b}")
print(f"Division : {a/b}")
print(f"Modulus : {a%b}")

print("\n--- Relational operators ---")
# Returns True or False
print(10 > 5)   # True
print(10 == 5)  # False
print(10 != 5)  # True

print("\n--- Logical operators ---")
# Includes Logical OR, AND, NOT
a = 10
b = 20

print(a > 5 and b > 15)  # True (Both must be true)
print(a > 5 or b < 15)   # True (At least one must be true)
print(not(a > 5))        # False (Reverses the result)


# ==========================================
# 6. Operator Precedence
# ==========================================
print("\n--- Operator Precedence ---")
# Sequence: () > {*/ // %} > + -
# print(10+2*5)   -> 2*5=10 -> 10+10 = 20
# print((10+2)*5) -> 10+2=12 -> 12*5 = 60


# ==========================================
# 7. Indentation & Comments
# ==========================================
print("\n--- Indentation & Comments ---")
# Indentation means empty spaces in python (used for blocks)

if a > 5:
    print(f"{a} > 5")

# Comments in Python:
"""
1. This is a multi-line comment
"""
# 2. This is a single-line comment


# ==========================================
# Practice Questions
# ==========================================

print("\n--- Practice 1: Swap two numbers (with temp) ---")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

temp = a
a = b
b = temp
print(f"Swapped values are \n a:{a} \n b:{b}")


print("\n--- Practice 2: Swap two numbers (without temp) ---")
a = int(input("Enter the first number: ")) # 10
b = int(input("Enter the second number: ")) # 20

# Logic:
a = a + b  # 10 + 20 = 30
b = a - b  # 30 - 20 = 10 (b becomes 10)
a = a - b  # 30 - 10 = 20 (a becomes 20)

print(f"Swapped values are \n a:{a} \n b:{b}")


print("\n--- Practice 3: Simple calculator ---")
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("Add:", a + b)
print("Sub:", a - b)
print("Mul:", a * b)
print("Div:", a / b)

# Chained Comparison Check
print(5 > 3 > 1)