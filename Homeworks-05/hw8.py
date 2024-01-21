"""import random
import string
import math



#Note. Try to clear the terminal if appropriate.
#
#- Comments -
#If it's appropriate:
#A. One-line comment 
#B. Multi-line comment
#
#- Programs -
#A. Write a program that asks user for their personal data (name, age, nationality).The program should decoratively print this values to the terminal.
print("Please enter your name,age and nationality.")
name = str(input("Name: "))
age = int(input("Age: "))
nationality = str(input("Nationality: "))
dcr = "\n>> " #Terminal decoration
print(f"{dcr}Your personal data is {name}, {age}, {nationality}")
#
#B. Write a simple calculator program that can only sum the values. If user inputs 10 and 5, the program should print 15
print("Simple calculator for sum the values:")
a = float(input("Enter first number: "))
b = float(input("Enter your second number: "))
print("Your answer is:", f">{a+b}<")
#
#C. Write a string calculator program that adds strings to strings. If user inputs:
#1. 'Hello' and 'World', the program should print 'HelloWorld'.
#2. 10 and 5, the program should print 105.
#3. 'Hello' and 10, the program should print Hello10
print("Simple calculator for sum the strings:")
a = str(input("Enter first string: "))
b = str(input("Enter second string: "))
print("Your answer is:", f">{a+b}<")
#
#- Modules -
#A. Which Python module provides a collection of string constants, such as ascii_letters?
#string

#B. If you want to create a password generator that includes both uppercase and lowercase letters, which constant from the 'string' module might be useful?
#ascii_letters
#
#C. What is the purpose of using constants like ascii_letters from the string module in Python programming?
#Constants are to increase the readability of the code. They make the written code easy to read for other programmers.
#
#D. What is 'getpass' function from 'getpass' module for?
#Prompt the user for a password without echoing
#
#- Python Tricks -
#A. Suppose you have the following variables:
##a = "Hello"
##b = 5
##
##One-line change the value of 'a' to value of 'b', and vice versa.
##Print their values
a = "Hello"
b = 5
b, a == a, b
print(a, b)
a, b == b, a
print(a, b)
##
##- Constants -
#import math
##A. Create a constant variable related to Mathematics.
PI = math.pi
#
##B. Create a constant variable related to Physics.
MOMENTUM = 100
#
##C. Create a constant variable related to Price.
PRICE = 250
#
##D. Create a constant variable related to Time.
MORNING = 6
#
##E. Are Python constants really carry constant values?
#No
##
##- Math -
##A. Round down 57_999.99 to the nearest integer.
a = 57999.99
print(math.floor(a))
#
##B. Find the square root of 57_999.99. Round it to one decimal point.
print(math.sqrt(a))
#
##C. Round up 0.0592481 to the nearest integer.
a = 0.0592481
print(math.ceil(a))
#
##D. Find the value of 5.5 raised to power 5.
a = 5.5
print(pow(a, 5))
##
##- NoneType -
##A. What is None in Python? How is this value described in other programming
##languages?
##In python None equal to void
#
##B. What is the best practices of using None in Python?
#
#
#
##C. How Python evaluates the NoneType? (True / False)
#False
##D. Create any NoneType object. Print it.
a = None
print(a)
#
##
##- Built-ins -
##A. Create two variables (x and y). Using built in function raise 'y' to 'x' power.
a = 5
b = 3
c = pow(a, b)
#
##B. Using built in function and variables from Task A raise 'x' to 'y' power.
#c = pow(b, a)
#
##C. Ask user for two integers. Raise first integer to second integer power.
a = int(input("First integer:"))
b = int(input("Second integer"))
c = pow(a, b)
print(f"your answer is: {c}")
##
##- String Formattings -
##A. You have the math's Pi number. Using f-strings, round it to two decimal points.
a = math.pi
b= f"{a:.2f}"
print(b)
#
##B. Write a program that represents 5_000_000 as (5,000,000) in console
a = 5000000
print(f"{a:,}")
#
##C. Write a program that calculates the percentage of apples left in the fridge.
##Initially you got 28 apples, but you ate 4. Using f-strings print the percentage
##of the apples left.
quantity = 28
eaten = 4
left = quantity - eaten
percentage = float(f"{(left / quantity) * 100}")
print(f"{percentage:.0f} percentage apples left in the fridge")

#
#- Chat GPT's Homework -
#1. What does the random.choice(seq) function do?
#B) Selects a random element from the sequence seq.
#
#2. How do you generate a random integer between 5 and 10 (inclusive) 
#using random.randint(a, b)?
a = random.randint(5, 10)
print(a)
#
#3. Write a code snippet that generates a random float between 0 and 1 
#(exclusive) using random.random().
a = random.random(0, 1)
print(a)
#
#4. What does the random.sample(seq, k) function do?
#B) Selects multiple unique random elements from the sequence.
#
#5. Calculate the square root of 25 using the math.sqrt() function.
a = 25
print(math.sqrt(a))

#
#6. How do you access the value of pi using the math module?
a = math.pi
#
#7. If you have a float value x = 7.6, how would you round it up to the nearest 
#integer using the math.ceil() function?
x = 7.6
print(math.ceil(x))

#8. Write a Python program that generates and prints 5 random integers between 
#50 and 100 (inclusive) using the random.randint() function.
a = random.randint(50, 100)
print(a)

#9. Write a Python program that takes a floating-point number as input and prints 
#its square root using the math.sqrt() function.
a = float(input("Enter a floating-point number: "))#user input
b = math.sqrt(a)
print(f"The square root of {a} is: {b}")

#10. Implement a Python "Roll Dice" program that simulates rolling a six-sided die. 
#The program should return a random number between 1 and 6.
six_sided_die = [1, 2, 3, 4, 5, 6]
number = random.randint(six_sided_die)
print(number)

#- Interview Questions -
#1. Reverse a string with slicing method.
a = "Elmir"
reverse_a = a[::-1]
print(reverse_a)

#
#Quiz.
#1. What does the None keyword represent in Python?
#    b) A placeholder for missing or undefined values
#
#2. Which type is assigned to a variable that has no value assigned to it in Python?
#    b) NoneType
#
#3. What is the result of evaluating the expression: type(None)?
#    a) <class 'NoneType'>
#
#4. Which statement assigns the value None to the variable 'result'?
#    b) result = None
#
#5. What is the correct way to check if a variable value is set to None?
#    d) if value is None:
#
#6. Can None be used in arithmetic operations in Python?
#    b) No, trying to perform arithmetic with None will result in an error.
#
#7. What does the math.floor(x) function do?
#    c) Rounds x to the nearest integer.
#
#8. Which of the following is the correct way to import the 'math' module in Python?
#    b) import math
#
#9. The math.ceil(x) function does what?
#    b) Returns the value of x rounded up to the nearest integer.
#
#10. What does the math.pow(x, y) function do?
#    c) Calculates the power of x raised to the yth power.
#
#11. The math.sqrt(x) function is used to:
#    a) Calculate the square root of x.
#
#12. What is the output of the following code:
#    import math
#    value = 3.05
#    print(math.floor(value))
#
#    a) 3
#
#13. What is the output of the following code:
#    from math import pi
#    a = round(pi, 2)
#    print(a * 2)
#
#    c) 6.28
#
#14. What is the purpose of the random.choice(seq) function?
#    b) It selects a random element from the sequence seq.
#
#15. Which of the following methods is used to select multiple unique random 
#elements from a sequence?
#    b) random.sample(seq, count)
#
#16. How would you import the random module correctly in Python?
#    d) import random
#
#17. If you want to generate a random integer between 1 and 100 (inclusive), 
#which random module method would you use?
#    a) random.randint(1, 100)
#
#18. In Python, what is the process of combining multiple strings into one?
#    a) Concatenation
#
#19. What does the ascii_letters constant include?
#    c) Both uppercase and lowercase letters
#
#20. Which PEP provides recommendations and guidelines for writing clean, readable, and maintainable Python code?
#    b) PEP 8
#
#21. What is the primary purpose of the "as" keyword in Python's "import" statement?
#    a) It renames the module being imported.
#"""
a = ["a", "b", "c"]
a.sort()
print(a)