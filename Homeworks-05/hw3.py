'''
#Note. Use clear and descriptive variable names throughout the code.
#Make sure to add comments to explain the purpose and functionality of 
#your code.
#
#- String Formattings -
#A. Create a variable called 'genre'. Give it a string value.
genre = "pop"

#B. Create a variable called 'producer'. Give it a string value.
producer = "Vasif"

#C. Create a variable called 'song'. Give it a string value.
song = "Dolya"

#D. Using three Python String Formatting types (f-strings, .format(), %s) create 3 variables accordingly to the formats count, and make it equal 
name = "Elmir" 
string = f"{name} was dead "
new_string = "{} was dead".format(name)
second_string = "%s was dead" % (name)
print(string, new_string, second_string, sep="\n")

#to little text (story) using all variables from Task A to C.
story = f"I listen to new {song} by {producer} and its genre is {genre}."
print(story)

#E. Create a variable called 'firstname'. Give it an appropriate value.
firstname = "Elmir"

#F. Create a variable called 'lastname'. Give it an appropriate value.
lastname = "Akmedov"

#G. Create a variable called 'age'. Give it an appropriate value.
age = 18

#H. Create a variable called 'gender'. Give it an appropriate value.
gender = "man"

#I. Using all of string formatting methods and variables from Task E to H, 
story_2 = "There is a {} and they called him {} {}.His age is {}".format(gender, firstname, lastname, age)
print(story_2)

"""
print as the following:
My name is John Smith, and I am 27 years old. My gender is - Male.
"""
firstname = "John"
lastname = "Smith"
age_2 = "27"
gender = "Male"
story_3 = "My name is %s %s,and I am %s years old. My gender is - %s" % (firstname, lastname, age_2, gender)

#J. Create a variable called 'language'. Make it equal 'Python'. Using f-strings
new = "Python"
language = f"{new}"

#print 'I love Python. I will repeat this word 5 times: PythonPythonPythonPythonPython.'
story_4 = f"I love {language}. I will repeat this word 5 times: {language*5}."
print(story_4)

#K. Create a variable called 'hello'. Make it equal 'Hello'.
hello =("Hello ")

#Create a variable called 'world'. Make it equal 'World'. 
world = "World"

#Using math operations and '.format' string-formatting method print 'Hello World!'.
hello_world = "{}".format(hello + world)
print(hello_world)
#L. Create a variable called 'date'. Make it equal the date of your birthday in
#the following format => "01.01.2001". Using '%s' string-formatting method print
#the following:
#My birth date is 01.01.2001.
date = "12.12.2004"
sentence = "My birtday is %s." % (date)
print(sentence)

#M. Create a text-story using all variables created through all tasks in this hworomek file. You should use multi-line strings.

name = f"{firstname} {lastname}"
work = "{} programist".format(language)
text_story = """Hello.
My name is %s.
I am a %s.
But i can't write codes correct.
""" % (name, work)
print(text_story)

#N. Create a variable with a string value that will contain 4 curly brackets (you will fill them soon). Additionally, create 4 different variables of any type on your own. Using '.format' string-formatting method and those 4 variables fill the previous string with 4 curly brackets. Print it
computer = "{comp_location}, {comp_name}, {comp_color}, {comp_location}".format(
    logo_color = "Gray",
    comp_name = "Asus",
    comp_color = "Black",
    comp_location = "Baku"
)
print(computer)

#
# O. Perform math operations with strings in a 'f-string' string-formatting method.
x = 25
y = 30
print(f"{x*y}")

#P. Create a variable called 'expression'. Give it any string value.
#Using a variable which you have created previously and contains 4 curly brackets print the 'expression's value 4 times using '.format' string-formatting method.
logo_color = "Gray"
comp_name = "Asus"
comp_color = "Black"
comp_location = "Baku"
expression = "{},{},{},{}".format(logo_color, comp_color, comp_name, comp_location)
print(expression)
#Quiz:
#A. In the following code, 'Hello' is a string literal. True or false?
#
#    ---------------------
#    |    s = 'Hello'    | 
#    ---------------------
#
#    a) True
#
#B. The two strings 'Hello' and "Hello" are identical to each other. Yes or no?
#    a) Yes
#
#C. Is there a problem in the code below? If yes, then how can we rectify it?
#
#    ------------------------------
#    |    s = 'Python's call!'    | 
#    ------------------------------
#
#    b) Yes, by using a backslash
#
#D. How to denote a multiline string in Python?
#
#    c) Using either (b) and (c)
#
#E. When used on strings, what does the * operator do?
#    a) Replicates them
'''
import time
start = time.time()
print(start)