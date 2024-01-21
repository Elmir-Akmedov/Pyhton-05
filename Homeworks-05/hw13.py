'''
#Instructions: Write Python code for each of the following tasks. 
#Make sure to use if statements appropriately to achieve the desired outcomes. 
#If appropriate, comment your code to explain each step.
#
#- If Statements -
#A. Create any variable with Boolean value. Print 'My variable evaluates to True'
#if this variable is 'True', otherwise print 'My variable evaluates to False'.
variable = False
if variable:
    print("My variable evaluates to True")
else:
    print("My variable evaluates to False")

#B. Create a variable named 'temperature'. Make it equal to any degree. Check:
#1. If temperature is under 10 degrees, print 'It\'s cold outside, take a scarf.'.
#2. If temperature is in interval from 10 to 24 degrees (both included), print 
#'It\'s a nice weather. Let\'s go for a walk.'.
#3. If temperature is above 24 degrees, print 'It\'s quite hot, I need an AC.'.
temperature = 36
if temperature < 10:
    print("It's cold outside, take a scarf.")
elif 10 <= temperature <= 24:
    print("It's a nice weather. Let\'s go for a walk.")
elif temperature > 24:
    print("It\'s quite hot, I need an AC.")
    

#C. Create a variable named 'age'. Make it equal your age. Check:
#1. If it's under 18, print 'I am not eligible for voting :('
#2.If you are 18 or older, print 'I am eligible for voting!'
age = 19
print("I am not eligible for voting :(") if age < 18 else print("I am eligible for voting!")

#D. Create variables 'a' and 'b'. Make them equal 15 and 20 correspondingly.
#Check if their sum gives less than 40, print their sum and add 'It\'s less than 40.'.
#Otherwise, print their sum and add 'It makes 40 or more than 40.'.
a = 15
b = 20
if a+b < 40:
    print(a + b, "It\'s less than 40.")
else:
    print(a + b, "It makes 40 or more than 40.")

#E. Create a list with 4 students (make it contain their names). Check if the 
#length of that list is less than 5, add new student to that list.
students = ["Elmir", "Seymur", "Ayxan", "Suphan"]
if len(students) < 5:
    students.append("Eldar")

#F. Create four variables (a, b, c, d) with numeric (int & float) values.
#Write the logical expression to check if 'a' is greater than 'b' and 'c' is greater
#than 'd'.
a, b, c, d = 1.1, 5, 5.6, 4
if a > b:
    print("'a' is greater than 'b'") 
else:
    print("Error")
if c > d:
    print("'c' is greater than 'd'") 
else:
    print("Error")

#G. Write a program to check whether a number accepted from user is divisible by 2
#and 3 both.
number = float(input("Write any number:\n>> "))
if number % 6 == 0:
    print("Your number is divisible by 2 and 3 both.")
else:
    print("Your number isn't divisible by 2 and 3 both.")

#H. Write a program that finds the largest number out of three numbers accepted from user.
numbers_list = [float(input("Write any number:\n>> ")) for i in range(3)]
print(f"Your list is:{numbers_list}")
largest_number = max(numbers_list)
#numbers_list.sort()
largest_number1 = numbers_list[-1]
print(f"The largest number in your list is:{largest_number1}")

#I. Write a program that gets any input from user. It should print 'Lower job!' if all
#characters in user's input are lowercase, otherwise print 'Upper job!'.
user_input = str(input("Enter any word"))
if user_input.islower():
    print("Lower job!")
else:
    print("Upper job!")

#J. Write a program to check whether a number entered by user is three digit number or not.
user_input = input("Enter any number:\n>> ")
if len(user_input) == 3:
    print("Your number digits is 3")
else:
    print("Your number digits isn't 3")

#K. Accept the temperature in degree Celcius of water and check whether it's boiling or
#not (boiling point of water is 100 degree Celcius).
temperature = float(input("Enter your water degree:\n>> "))
if temperature < 100:
    print("It's boiling")
else:
    print("It isn't boiling")


#L. Accept the IQ of 3 people and display the highest one.
numbers_list = [float(input("Write any number:\n>> ")) for i in range(3)]
print(f"Your list is:{numbers_list}")
#largest_number = max(numbers_list)
numbers_list.sort()
largest_number1 = numbers_list[-1]
print(f"The largest number in your list is:{largest_number1}")

#M. Write a program to check whether a character accepted from user is vowel or not.
vowels = ["a", "e", "o", "i", "u"]
user_input = str(input("Enter any character:\n>> ")).lower()
if user_input in vowels:
    print("Your character is vowel.")
else:
    print("Your character isn't vowel.")

#N. Accept the following from the user and calculate the percentage of class attendance:
#1. Total number of class days
#2. Total number of days for absence
total_days = int(input("Total number of class days"))
total_absence = int(input("Total number of days for absence"))
percentage = ((total_days - total_absence) / total_days) * 100
print(f"{percentage}%")

#O. Accept the percentage from the user and display the grade according to the following
#criterias:
#1. Below 25 - D
#2. 25 to 45 - C
#3. 45 to 50 - B
#4. 50 to 60 - B+
#5. 60 to 80 - A
#6. Above 80 - A+
percentage = int(input("Your percentage:\n>> "))
if percentage < 25:
    print("D")
elif percentage < 45:
    print("C")
elif percentage < 50:
    print("B")
elif percentage < 60:
    print("B+")
elif percentage < 80:
    print("A")
else:
    print("A+")

#
#- Dictionary Methods -
#A. Create a nested dictionary. Get any inner value using multiple key-indexing.
user_dictionary = {
    "Office_Laptop": {},
    "Gaming_Laptop": {}
}
user_dictionary = ""'''
#B. Create a dictionary with your personal data (name, surname, age, family status,
#gender). Ask user for any key in your dictionary. Print the value of the given
#key from the dictionary. Try to ask all keys.
#C. Create a dictionary with stock data of clothes (cloth name + amount). Let 
#the user choose any of keys and add some count to it.
#D. Copy any dictionary from previous tasks. Print it.
#E. Clear the dictionary from Task D. Print the length of this dictionary.
#F. Create an empty dictionary. Let the user add data to it (key & value). Choose
#any topic (books, cars, info, items, grades...) and let the user fill it with
#minimum 4 key-value pairs.
#G. You have the following dictionary:
#car = {
#    "brand": "Chevrolet",
#    "model": "Camaro",
#    "year": 2017
#}
#
#Create a 'not_found_message' variable. Make it equal appropriate "not found" message.
#Try to get 'year's and 'color's values from the 'car'. Set the default value to 
#our "not found" message.
#H. Print the first 6 keys from the following dictionary (hint: you should use 
#'list()' method to convert dict_keys to list and indexing to get the appropriate
#portion of data):
#countries_capitals = {
#    "USA": "Washington, D.C.",
#    "Canada": "Ottawa",
#    "United Kingdom": "London",
#    "France": "Paris",
#    "Germany": "Berlin",
#    "Japan": "Tokyo",
#    "Australia": "Canberra",
#    "Brazil": "Brasília",
#    "India": "New Delhi",
#    "South Africa": "Pretoria",
#}
#I. You have the following dictionary:
#programming_languages = {
#    "Python": {
#        "designed_by": "Guido van Rossum",
#        "first_appeared": 1991,
#        "paradigm": "Multi-paradigm",
#        "typing": "Dynamic",
#        "popularity": "High"
#    },
#    "JavaScript": {
#        "designed_by": "Brendan Eich",
#        "first_appeared": 1995,
#        "paradigm": "Multi-paradigm",
#        "typing": "Dynamic",
#        "popularity": "Very High"
#    },
#    "Java": {
#        "designed_by": "James Gosling",
#        "first_appeared": 1995,
#        "paradigm": "Object-oriented",
#        "typing": "Static",
#        "popularity": "High"
#    },
#    "C++": {
#        "designed_by": "Bjarne Stroustrup",
#        "first_appeared": 1985,
#        "paradigm": "Multi-paradigm",
#        "typing": "Static",
#        "popularity": "Moderate"
#    }
#}
#
#Using in f-strings print the year Python was appeared value.
#J. You have the following code snippet:
#tasks = {
#    "Alice": ["Buy groceries", "Finish report", "Call the doctor"],
#    "Bob": ["Walk the dog", "Pay bills", "Read a chapter"]
#}
#
#selected_person = "Alice"
#new_task = "Go to the gym"
#
#Add the new task to the selected person's tasks. Print the tasks & length of tasks 
#before and after edition.
#K. There is a dictionary method that helps to create a dictionary with a collection
#of keys and apply a default value to that key. Using that method create a dictionary
#with all values equal to the '[0, 4, 8, 12, 16, 20]' list and keys should only be
#the numbers from 0 to 4, so your dictionary should look like:
#digits = [1, 2, 3, 4, 5]
#
#my_dict = {
#    0: [0, 4, 8, 12, 16, 20],
#    1: [0, 4, 8, 12, 16, 20],
#    2: [0, 4, 8, 12, 16, 20],
#    3: [0, 4, 8, 12, 16, 20],
#    4: [0, 4, 8, 12, 16, 20],
#}
#
#You should use list comprehension in this task.
#
#Then you should print some portion from the list values of a dictionary. The
#portion size depends on a key you are using to index the list.
#L. Print all items, values, keys from 'programming_languages' dictionary.
#M. Remove 'Java' from 'programming_languages' dictionary & get its value. Print it.
#N. Remove the last item from the following dictionary and print it:
#car = {
#    "brand": "Ford",
#    "model": "Mustang",
#    "year": 1964
#}
#O. Expand 'programming_languages' dictionary with the following data:
#language_to_add = {
#    "PHP": {
#        "designed_by": "Rasmus Lerdorf",
#        "first_appeared": 1995,
#        "paradigm": "Server-side scripting",
#        "typing": "Dynamic",
#        "popularity": "Moderate"
#    }
#}
#P. Use 'setdefault' method on any dictionary.
#Q. Which Data Types can be represented as values of any dictionary?
#R. In the following example:
#data = {
#    "Python3.x": {
#        "Wep Development", "Machine Learning", "Penetration Testing", "Game Development"
#    }
#}
#
#It's giving an error if you try to get 'Python2.x' in this way:
#data["Python2.x"]
#Edit this code so it doesn't return an error.
#
#- Chat GPT's Homework -
#Task 1.
#Create an empty dictionary called student_info.
#Add the following key-value pairs to the dictionary:
#"name": "John Doe"
#"age": 20
#"major": "Computer Science"
#
#Task 2.
#Print the value associated with the key "name" from the student_info dictionary.
#Change the value of the "age" key to 21.
#Add a new key-value pair: "gender": "Male".
#
#Task 3.
#Create a new dictionary called grades with the following data:
#"math": 85
#"english": 92
#"history": 78
#Use the update method to add the key-value pairs from the grades dictionary into the student_info dictionary.
#
#Task 4.
#Remove the "history" key from the grades dictionary using the pop method, and print the value that was removed.
#Remove the "major" key from the student_info dictionary using the del statement.
#
#Task 5: Basic If-Else Statements
#Write a Python program that does the following:
#Takes an integer input from the user.
#Checks if the input is greater than 10.
#If it is, prints "The number is greater than 10."
#If it's not, prints "The number is not greater than 10."
#
#Task 6: Multiple Conditions
#Write a Python program that:
#Takes two integer inputs from the user.
#Checks if both numbers are even (divisible by 2).
#If both are even, prints "Both numbers are even."
#If at least one is not even, prints "At least one number is not even."
#
#Task 7: Grade Calculator
#Write a Python program that:
#Takes a numerical score as input from the user (0 to 100).
#Uses if-elif-else statements to determine the corresponding letter grade based on the following scale:
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: 0-59
#Prints the calculated letter grade.
#
#Task 8: Leap Year Checker
#Write a Python program that:
#Takes a year as input from the user.
#Checks if the year is a leap year or not.
#A leap year is divisible by 4, but not divisible by 100 unless it's also divisible by 400.
#Prints "Leap year" or "Not a leap year" accordingly.
#
#Task 9: Temperature Converter
#Write a Python program that:
#Takes a temperature in Celsius as input from the user.
#Converts it to Fahrenheit using the formula: Fahrenheit = (Celsius * 9/5) + 32.
#Prints the temperature in Fahrenheit.
#
#Task 10: Number Comparison
#Write a Python program that:
#Takes three integer inputs from the user.
#Determines and prints the largest of the three numbers using if-else statements.
#
#Task 11: Positive or Negative
#Write a Python program that:
#Takes an integer as input from the user.
#Checks if the number is positive, negative, or zero.
#Prints "Positive," "Negative," or "Zero" accordingly.
#
#Task 12: Eligibility Checker
#Write a Python program that:
#Takes the age and citizenship status (True for U.S. citizen, False for non-U.S. citizen) as input from the user.
#Checks if the person is eligible to vote in the U.S. based on the following conditions:
#Must be at least 18 years old.
#Must be a U.S. citizen.
#Prints "You are eligible to vote" or "You are not eligible to vote" accordingly.

user_age = int(input("Enter your age:"))
user_citizenship = input()
#Task 13: Password Strength Checker
#Write a Python program that:
#Takes a password as input from the user.
#Checks the strength of the password based on the following criteria:
#At least 8 characters long.
#Contains both uppercase and lowercase letters.
#Contains at least one digit (0-9).
#Prints "Strong password" or "Weak password" accordingly.
'''
password = input("Enter password -> ")  
if (len(password)) >= 8: 
    if not password.isdigit() and not password.isalpha(): 
        if password.isupper and password.islower: 
            print("Strong password")  
                
        else: 
            print("Weak passwor")
    else: 
        print("Weak password")  
else: 
    print("No longer than 8 characters!!!")
...
#Task 14: Rock-Paper-Scissors Game
#Write a Python program that:
#Implements a simple text-based rock-paper-scissors game.

#Takes the player's choice as input (rock, paper, or scissors).
#Generates a random choice for the computer.
#Determines the winner based on the game rules.
#Prints the result of the game (win, lose, or tie) and the computer's choice.
from random import choice


print("::::::Rock,Paper,Scissors game::::::")
base_game = ["rock", "paper", "scissors"]
user_input = input("Enter your choice:(rock, paper, or scissors)\n>> ").strip().lower()
computer_choice = choice(base_game)

if user_input in base_game:
    for _ in range(5):
        if user_input == computer_choice:
            print("Tie")
        elif user_input == "rock" and computer_choice == "scissors":
            print("You won...")
        elif user_input == "scissors" and computer_choice == "paper":
            print("You won...")
        elif user_input == "paper" and computer_choice == "rock":
            print("You won...")
        else:
            print("I won... :)")
        print(f"My choice is:{computer_choice}")
        break
else:
    print("Your choice must be rock,paper or scissors!!!")
'''
#- Comments -
#A. One-line comment in any random three places of your code, if it's appropriate.
#B. Multi-line comment anywhere in your code, if it's appropriate.
#
#
#
#Quiz. (If-Statements)
#1. What is the keyword used to define an 'if' statement in Python?
#    a) if
#    b) case
#    c) switch
#    d) when
#
#2. How do you write an if statement in Python?
#    a) if condition:
#    b) if (condition)
#    c) if {condition}
#    d) if [condition]
#
#3. In Python, what is the symbol for 'not equal to' in an if statement?
#    a) ==
#    b) !=
#    c) <=
#    d) >=
#
#4. In Python, what is the purpose of the 'elif' statement?
#    a) It is used for error handling.
#    b) It is executed if the 'if' condition is True.
#    c) It is executed if the 'if' condition is False.
#    d) It is executed if the 'if' condition is True, and no 'else' condition is present.
#
#5. What will be the output of the following Python code?
#    if 10 > 5:
#        print("10 is greater than 5")
#    else:
#        print("This will not be printed")
#
#    a) 10 is greater than 5
#    b) This will not be printed
#    c) SyntaxError
#    d) 5 is greater than 10
#
#6. What is the output of the following Python code?
#    x = 15
#    if x < 10:
#        print("x is less than 10")
#    elif x < 20:
#        print("x is less than 20 but greater than or equal to 10")
#    else:
#        print("x is 20 or greater")
#
#    a) x is less than 10
#    b) x is less than 20 but greater than or equal to 10
#    c) x is 20 or greater
#    d) x is 15
#
#7. What is the primary purpose of an 'if' statement in Python?
#    a) To execute a specific block of code based on a condition.
#    b) To create loops in a program.
#    c) To define a function.
#    d) To print output to the console.
#
#8. When is an 'else' statement used in conjunction with an 'if' statement?
#    a) To execute the code block if the 'if' condition is True.
#    b) To execute the code block if none of the 'if' or 'elif' conditions are True.
#    c) To execute the code block regardless of the 'if' condition.
#    d) To define a loop within the 'if' statement.
#
#9. Consider the following Python code. What will be printed if the variable 'num' is greater than or equal to 20?
#    num = 25
#    limit = 20
#
#    if num >= limit:
#        print("The number is greater than or equal to the limit")
#    else:
#        print("The number is less than the limit")
#
#    a) The number is greater than or equal to the limit
#    b) The number is less than the limit
#    c) The number is exactly the limit
#    d) There is a syntax error in the code
#
#10. Given the Python code snippet:
#    num = 15
#
#    if num > 10:
#        print("num is greater than 10")
#
#    What will be the output if this code is executed?
#
#    a) num is greater than 10
#    b) num is less than 10
#    c) num is 10
#    d) num is equal to 15
#
#11. Given the Python code snippet:
#    x = 15
#
#    if x > 10 and x < 20:
#        print("x is greater than 10 and less than 20")
#    else:
#        print("x is either less than or equal to 10 or greater than or equal to 20")
#
#    What will be the output if this code is executed?
#    a) x is greater than 10 and less than 20
#    b) x is either less than or equal to 10 or greater than or equal to 20
#    c) x is 10
#    d) x is 20
#
#12. Given the Python code snippet:
#    y = 5
#
#    if y < 0 or y > 10:
#        print("y is less than 0 or greater than 10")
#    else:
#        print("y is between 0 and 10 (inclusive)")
#
#    What will be the output if this code is executed?
#    a) y is less than 0 or greater than 10
#    b) y is between 0 and 10 (inclusive)
#    c) y is 0
#    d) y is 10
#
#13. Given the Python code snippet:
#    x = 8
#
#    if x < 10:
#        print("Code block 1: x is less than 10")
#    elif x < 15:
#        print("Code block 2: x is less than 15")
#    elif x < 20:
#        print("Code block 3: x is less than 20")
#    else:
#        print("Code block 4: x is 20 or greater")
#
#    What will be the output if this code is executed when x is 8?
#    a) Code block 1: x is less than 10
#    b) Code block 2: x is less than 15
#    c) Code block 3: x is less than 20
#    d) Code block 4: x is 20 or greater
#
#14. Given the Python code snippet:
#    y = 25
#
#    if y < 10:
#        print("Code block 1: y is less than 10")
#    elif y < 15:
#        print("Code block 2: y is less than 15")
#    elif y < 20:
#        print("Code block 3: y is less than 20")
#    else:
#        print("Code block 4: y is 20 or greater")
#
#    What will be the output if this code is executed when y is 25?
#    a) Code block 1: y is less than 10
#    b) Code block 2: y is less than 15
#    c) Code block 3: y is less than 20
#    d) Code block 4: y is 20 or greater
#        
#Quiz. (Dictionaries)
#1. Which of the following are true of Python dictionaries:
#    a) Dictionaries are mutable
#    b) Items are accessed by their position in a dictionary
#    c) A dictionary can contain any object type except another dictionary
#    d) Dictionaries can be nested to any depth
#    e) Dictionaries are accessed by key
#    f) All the keys in a dictionary must be of the same type
#
#2. Consider this dictionary:
#    d = {'foo': 100, 'bar': 200, 'baz': 300}
#    What is the result of this statement:
#    d['bar':'baz']
#
#    a) (200, 300)
#    b) [200, 300]
#    c) 200 300
#    d) It raises an exception
#
#3. Suppose x is defined as follows:
#    x = [
#        'a',
#        'b',
#        {
#            'foo': 1,
#            'bar':
#            {
#                'x': 10,
#                'y': 20,
#                'z': 30
#            },
#            'baz': 3
#        },
#        'c',
#        'd'
#    ]
#
#What is the expression involving x that accesses the value 30?
#
#4. Select the correct ways to get the value of marks key.
#    student = {
#    "name": "Emma",
#    "class": 9,
#    "marks": 75
#    }
#
#    a) m = student.get(2)
#    b) m = student.get('marks')
#    c) m = student[2])
#    d) m = student['marks'])
#
#5. Dictionary keys must be immutable:
#    a) True
#    b) False
#
#6. Select the all correct way to remove the key marks from a dictionary:
#    student = { 
#        "name": "Emma",
#        "class": 9,
#        "marks": 75
#    }
#
#    a) student.pop("marks")
#    b) del student["marks"]
#    c) student.remove("marks")
#    d) student.popitem("marks")
#
#7. What is the output of the following dictionary operation:
#    dict1 = {"name": "Mike", "salary": 8000}
#    temp = dict1.get("age")
#    print(temp)
#
#    a) KeyError: 'age'
#    b) None
#
#8. Items are accessed by their position in a dictionary and all the keys in a 
#dictionary must be of the same type:
#    a) True
#    b) False
#
#9. Select all correct ways to copy a dictionary in Python:
#    a) dict2 = dict1.copy()
#    b) dict2 = dict(dict1)
#    c) dict2 = dict1
#
#10. Please select all correct ways to empty the following dictionary:
#    student = { 
#        "name": "Emma", 
#        "class": 9, 
#        "marks": 75 
#    }
#    a) del student
#    b) del student[0:2]
#    c) student.clear()
#
#11. What is the output of the following:
#    sample_dict = dict([
#        ('first', 1),
#        ('second', 2),
#        ('third', 3)
#    ])
#    print(sampleDict)
#
#    a) [ ('first', 100), ('second', 200), ('third', 300) ]
#    b) Options: SyntaxError: invalid syntax
#    c) {'first': 1, 'second': 2, 'third': 3}
#
#12. Select the correct way to access the value of a history subject:
#    sample_dict = {
#        "class": {
#            "student": {
#                "name": "Mike",
#                "marks": {
#                    "physics": 70,
#                    "history": 80
#                }
#            }
#        }
#    }
#
#    a) sample_dict['class']['student']['marks']['history']
#    b) sample_dict['class']['student']['marks'][1]
#    c) sample_dict['class'][0]['marks']['history']
#
#13. Select the correct way to print Emma's age:
#    student = {
#        1: {'name': 'Emma', 'age': '27', 'sex': 'Female'},
#        2: {'name': 'Mike', 'age': '22', 'sex': 'Male'}
#    }
#
#    a) student[0][1]
#    b) student[1]["age"]
#    c) student[0]["age"]
#
#14. What is the output of the following dictionary operation:
#    dict1 = {"name": "Mike", "salary": 8000}
#    temp = dict1.pop("age")
#    print(temp)
#
#    a) KeyError: 'age'
#    b) None
#
#15. What is the output of the following code:
#    dict1 = {"key1": 1, "key2": 2}
#    dict2 = {"key2": 2, "key1": 1}
#    print(dict1 == dict2)
#
#    a) True
#    b) False
#
#16. Select correct ways to create an empty dictionary:
#    a) sample_dict = { }
#    b) sample_dict = dict()
#    c) sample_dict = dict{}
#