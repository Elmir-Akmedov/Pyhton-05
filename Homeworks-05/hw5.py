import pywifi
"""
- I/O -
Warning! 1. You should set appropriate variable names each time when
you create a variable. 2. You should ask users appropriate questions.
3. Pay attention to the question style, try to decorate it.
"""
'''
#A. Write a program that asks user for his/her name. Print the name in capitalized form, so if the user types in 'aysel', we should see 'Aysel' on the console.
name = input("What is your name?\n>> ")
print(f"Your name is: {name.capitalize()}")

#B. Ask user for their age. Subtract this age from 50.
age = int(input("How old are you?\n>> "))
print(50 - age)

#C. Ask user for their address, favorite color, car brand.Using multi-line string formatting print this values using it in a sentence.
adress = input("What is your adress?\n>> ")
color = input("What is your favourite color?\n>> ")
car_brand = input("What is your car brand?\n>> ")
print(f"""Your adress is {adress}, 
your favourite color is {color}, 
      your car brand is {car_brand}"""
      )
#D. Write a calculator that plusses user's inputted numbers.
print(eval(input("New type of calculator, please enter numbers:\n>> ")))

#E. Write a calculator that subtracts user's inputted numbers.
a = int(input("This is for substract your inputted. Please enter your numbers:\n>> "))
b = int(input(">> "))
print(f"{(a - b)}")

#F. Write a calculator that multiplies user's inputted numbers.
a = int(input("This is for multiplies your inputted. Please enter your numbers:\n>> "))
b = int(input(">> "))
print(f"{(a * b)}")

#G. Write a calculator that divides user's inputted numbers.
a = int(input("This is for divides your inputted. Please enter your numbers:\n>> "))
b = int(input(">> "))
print(f"{(a / b)}")

#H. Ask user for 3 different numbers. Multiply first two numbers and then divide the result by the third inputted number.
a, b, c = int(input("Please enter 3 numbers:\n>> ")), int(input(">> ")), int(input(">> "))
print(int((a + b)/c))

#I. Write a program that prints the length of user's full name.
print(len(str(input("Please enter your name for find your name lenght:\n>> "))))

#J. Write a program that asks user for some Float number. This program soon will round this float number. Additionally, we need to ask for how many decimal digits user want to round it to. Print its rounded value.
a = float(input("Write number which you want to round:\n>> "))
b = int(input("How many decimal digits you want to round?:\n>> "))
print(round(a, b))

#K. Write a program that asks for 2 numbers. 1st number is the main number, and the 2nd number is for the power the user wants the 1st number to raise to. So if the 1st number is 16, and the 2nd is 2, we should see 256 on the console.
print(int(float(input("Main number:\n>> "))**int(input("how many times to raise the power\n>> "))), "\nThe answer is:")

#L. Write a program that asks user for any single word. Then ask for any number, because we will call String's 'center' method and give it the number user inputted.
word = str(input("Enter any word please:\n>> "))
number = int(input("Please enter any number you want:\n>> "))
print(word.center(number))

#M. Write a program that asks 'How many times should the program type "Python" word?'. Print the 'Python' word given number times. For example, if user gives us the 5 number, we should see on console: PythonPythonPythonPythonPython
name = str(input("Please any name enter:\n>> "))
times = int(input(f"How many times should the program type \"{name}\" word?:"))
print(name*times)

#N. Write a program that asks user for any sentence. The program should replace all characters in the sentence with its capitalized form. Given "I love the Python", the program should give us: I LOVE THE PYTHON
print(str(input("Please enter any sentence which you want to capitalized form:\n>> ")).upper())

#O. Write a program that asks user for any sentence. The program should replace all 'a' character in the sentence with 'o'. Given "Today is a great day!", the program should give us: Todoy is o greot doy!
print(str(input("Please enter any sentence which you want to replace all \"a\" to \"o\":\n>> ")).replace("a", "o"))

#P. Write a program that asks user for any input. The program should print 'True' if all characters in the input are lower characters.
print(str(input("Please enter any eord or sentence:\n>> ")).islower())

#Q. Write a program that asks user for any input. The program should print 'True' if all characters in the input are digits.
print(input("Please enter any eord or sentence:\n>> ").isdigit())

#R. Write a program that asks user for any phrase. The program should also ask for the amount the phrase will be printed. Depending on that amount print the user's phrase to terminal output.
name = str(input("Please any name enter:\n>> "))
times = int(input(f"How many times should the program type \"{name}\" word?:"))
print(name*times)

#S. Write a program that asks user for any amount. Depending on that amount you should print the stars before and after the 'Hello world' phrase. Example: (Amount is 3) *** Hello world ***
a = int(input("Please enter any number:\n>> "))
print("*"*a, "Hello word", "*"*a)

#- Chat GPT's Homework -
#Task 1. Create a Python program that greets the user and asks for their name.Use the input() function to receive the user's input and then print a personalized greeting.
a = str(input("Please enter your name:\n>> "))
print(f"Welcome Mr {a.capitalize()}")

#Task 2. Extend the program from Task 1 to ask the user for their birth year and calculate their age. Display a message that includes their name and age.
a = str(input("[Please enter your name:]\n>> "))
b = 2023 - int(input("[Please enter your birth year:]\n>> "))
print(f"[Welcome Mr {a.capitalize()}]\n[Your age is successfully calculate:{b}]")

#Task 3. Write a program that takes two numbers as input from the user and performs the following math operations:
a = str(input("[Please choose waht you want to do(\"Addition\",\"Subtraction\",\"Multiplication\",\"Division\"]\n>> ")).lower()

if a == "addition": #A. Addition
      print("[Your answer is:]\n>> ", int(input(">> ")) + int(input(">>")))
elif a == "subtraction": #B. Subtraction
      print("[Your answer is:]\n>> ", int(input(">> ")) + int(input(">> ")))
elif  a == "multiplication": #Multiplication
      print("[Your answer is:]\n>> ",int(input(">> ")) + int(input(">> ")))
elif  a == "division": #Division
      print("[Your answer is:]\n>> ", int(input(">> ")) + int(input(">> ")))
else :
      print("Please,write correctly")

#Task 4. Create a program that calculates the area of a triangle. Ask the user for the necessary inputs for calculations. 
a = int(input("Please enter the base lenght:\n>> "))
b = int(input("Please enter the height of base:\n>> "))
print(f"Your answer is: {1/2*a*b}")

#Task 5. Create a program that calculates the area of a rectangle. Ask the user for the necessary inputs for calculations. 
print("\"The area of the rectangle\"")
a = int(input("Please enter the lenght of rectangle:\n>> "))
b = int(input("Please enter the wide of rectangle:\n>> "))
print(f"Your answer is: {a*b}")

#Task 6. Create a program that calculates the area of a square. Ask the user for the necessary inputs for calculations. 
a = int(input("Please enter your one side lenght of square:\n>> "))
print(f"Your answer is: {a**2}")

#Task 7 (Extra!). For an extra challenge, implement a unit conversion feature.  Ask the user for a distance in meters and convert it to feet and inches.  There are approximately 3.28084 feet in a meter and 39.3701 inches in a meter.  Display the converted distances.
#Meter converter
a = float(input("Please enter your number for convert to inch and feet:\n>> "))
print("Your converted numbers is:\n", f"[{a*3.28084} feet, {a*39.3701} inch]")

#Quiz:
#1. Which of the following functions is used to convert a value to an integer in Python?
#           a) int()
#
#2. When using the input() function in Python, what data type is the input value 
#stored as by default?
#    c) str
#
#3. You want to find out how many characters are in a user-inputted sentence. 
#Which Python function would you use?
#    c) len()
#
#4. If a user enters "3.14159" as input using the input() function, how can you 
#convert it to a floating-point number?
#    a) float(input())
#
#5. If a user enters "5.7" as input using the input() function and you use 
#int(input()) for conversion, what will happen?
#    c) The decimal part will be truncated, resulting in 5.
#
#6. You want to display the length of a user-inputted string "Hello, World!" with a 
#descriptive message. Which option achieves this?
#    a) print("The length of the input is:", len(input()))
#
#7. What happens if a user enters "42" as input and you use float(input()) for 
#conversion?
#    b) The value is converted to the floating-point number 42.0..
#
#8. To style the user prompt and concatenate it with a variable, which option is correct?
#    b) input("Enter your name: ") + name
'''
int(input())