"""
#- For Loops -
#A. Write a program that uses a for loop to iterate over the numbers 
#from 1 to 10 (inclusive) using the range method. Print each number.
for x in range(1, 10):
    print(x)

#B. Create a list of fruits with at least 5 fruits. Use a for loop to 
#iterate over the list and print each fruit.
fruits = ["Orange", "Lemon", "Apple", "Banana", "Melon"]
for r, v in enumerate(fruits):
    print(f"{r + 1}. {v}")

#C. Write a program that takes a string input from the user and uses a 
#for loop to iterate over the characters in the string. Print each character.
user_input = input()
for x in user_input:
    print(x)

#D. Create a dictionary with at least 3 key-value pairs where keys are names 
#and values are ages. Use a for loop to iterate over the dictionary and print 
#each name and age pair.
data = {
    "Elmir" : 19,
    "Seymur" : 17,
    "Suphan" : 20
}
for x, v in data.items():
    print(f"{x}: {v}")

#E. Create a list of dictionaries where each dictionary represents a person 
#with a name and an age. Use a for loop to iterate over the list and print
#the name and age of each person.
data_list = [
    {"Name": "Elmir",
      "age": 25},
    {"Name": "Seymur",
      "age": 30},
    {"Name": "Suphan",
      "age": 22},
    {"name": "Turan",
      "age": 28},
]
for x in data_list:
    for k, v in x.items():
        print(f"{k}: {v}")

#F. Write a program that calculates and prints the factorial of a number 
#entered by the user. Use a for loop.
factorial = 1
print("Please enter a number for calculates the factorial of number: ")
user_number = int(input(">> "))
for x in range(1, user_number + 1):
    factorial *= x
    x += 1
print(f"Your answer is: {factorial}")

#G. Write a program that takes a number from the user and prints a pattern using 
#a for loop. For example, if the user enters 5, the output should be:
#*
#**
#***
#****
#*****
c = 5
d = 1
for x in range(c):
    print(f"{"*"*(d)}")
    d += 1

#H. Write a program that takes a list of numbers as input from the user 
#and uses a for loop to find and print the sum of all even numbers in the list.
print("Please enter numbers for sum of all even numbers:")
numbers = float[input(">> ")]
even_numbers = []
for x in numbers:
    if x % 2 == 0:
        even_numbers.append(x)
print(f"Your answer is: {sum(even_numbers)}")
"""
#I. What is the purpose of a for loop in Python, and how is it different from a while loop?
"""
Now I use "for loop" for iteretaion and i don't know about "while loop" yet
"""
"""
#J. Write a Python for loop that prints the numbers from 1 to 5 (inclusive).
for x in range(1, 6):
    print(x)

#K. Given a list of names: names = ['Alice', 'Bob', 'Charlie', 'David'], write a Python for 
#loop to print each name.
names = ['Alice', 'Bob', 'Charlie', 'David']
for x in names:
    print(x)

#L. Using a for loop, calculate the sum of all odd numbers from 1 to 10 (inclusive).
odd_numbers = []
for x in range(10):
    if x % 2 != 0:
        odd_numbers.append(x)
print(f"Your answer is: {sum(odd_numbers)}")

#M. Explain the concept of iterating over a string using a for loop. Provide a Python 
#code snippet that demonstrates this concept.
string = "Elmir"
for x, y in enumerate(string):
    print(f"{x}. {y}")

#N. Write a Python for loop that iterates over a range of numbers from 1 to 10 (inclusive) 
#and prints the square of each number.
for x in range(1, 11):
    print(x**2)

#O. You have the following tuple:
#numbers = (10, 20, 30, 40, 50)
#Iterate over this tuple and print the number if it's above 25.
numbers = (10, 20, 30, 40, 50)
for x in numbers:
    if x > 25:
        print(x)

#P. Write a program that uses a for loop to find and print the largest number in a given list.
#Don't use 'max' method.
print("Please enter numbers with spaces to find and print the largest number :")
given_list = [float(x) for x in input(">> ").split() ]
for x in range(len(given_list) - 1):
    smallest = min(given_list)
    given_list.remove(smallest)
print(given_list)
"""
#Q. Write a Python program that uses a for loop to print the multiplication table (up to 10) 
#for a given number.
for x in range(1, 10):
    for y in range(1, 10):
        print(f"{y}. {x} x {y}= {x * y}")
    print()
"""
"""
#Quiz.
#1. Consider the following Python code:
#    for i in range(5):
#        print(i)
#
#    What will be the output of this code?
#    a) 0 1 2 3 4
#
#2. Consider the following Python code:
#    total = 0
#    for i in range(1, 6):
#        total += i
#    print(total)
#
#    What will be the output of this code?
#    a) 15
#
#3. Consider the following Python code:
#    numbers = [10, 20, 30, 40, 50]
#    for num in numbers:
#        print(num)
#
#    What will be the output of this code?
#    a) 10 20 30 40 50
#
#4. Consider the following Python code:
#    word = "Python"
#    for char in word:
#        print(char * 3)
#
#    What will be the output of this code?
#    a) PPPyyyttthhhooonnn
#
#5. How do you define a for loop in Python?  
#    a) for i in range(n):
#
#6. What will the following code output?
#    numbers = [1, 2, 3, 4, 5]
#    for num in numbers:
#        print(num * 2)
#
#    b) 2 4 6 8 10
#
#7. How do you iterate over a dictionary using a for loop in Python?
#    c) for key, value in dictionary.items():
#
#8. What is the range function used for in a for loop?
#    c) To determine the length of a sequence
#
#9. What is the correct way to nest for loops in Python?
#    a) By placing one for loop inside another
#
#10. In Python, what is the output of the following loop?
#    for i in range(3):
#        print(i, end=' ')
#
#    a) 0 1 2
#
#11. Which of the following statements is true about the range function in Python?
#    a) It generates a sequence of numbers.
#
#12. In Python, how do you iterate through a list in reverse order using a for loop?
#    d) for i in list[::-1]:
#
#13. Which of the following data types can you iterate over using a for loop in Python?
#    a) String
#
#14. What is the correct syntax for a nested for loop in Python?
#    a)
#    for i in range(5):
#        for j in range(3):
#            print(i, j)
#
#15. In Python, what is immutability?
#    a) The ability of an object to be changed after it is created
#
#16. Which of the following data types in Python is immutable?
#    b) Tuples
#        
#17. What is the primary difference between a tuple and a list in Python?
#    d) Tuples are immutable, and lists are mutable
#
#18. What is an iterable in Python?
#    c) An object that can be looped over using a for loop
#
#19. Which of the following is NOT an example of an iterable in Python?
#    b) Integer
#
#20. What is the purpose of the iter() function in Python?
#    d) It reverses the elements of an iterable
#
#21. Which method is used to advance an iterator in Python?
#    a) next()
#
#22. What is the purpose of the next() function in Python?
#    a) It retrieves the next element from an iterator
#
#23. Which exception is raised when the next() function is called on an exhausted iterator in Python?
#    d) IterationError
#
#24. What will the following code output?
#    my_list = [1, 2, 3, 4, 5]
#    my_iterator = iter(my_list)
#    print(next(my_iterator))
#    print(next(my_iterator))
#    print(next(my_iterator))
#    print(next(my_iterator))
#    print(next(my_iterator))
#
#    a) 1 2 3 4 5      
#
#25. What is the correct way to use a for loop with an iterator in Python?
#    b) Use for element in iter(iterator):
#
#26. How can you use a for loop to iterate a specific number of times and prompt 
#the user for input within the loop?
#    c)
#    for i in range(int(input("Enter the number of times: "))):
#        user_input = input("Enter a value: ")
#
#27. How can you use a for loop to iterate over a list of names and print 
#a customized greeting based on each name?
#    a)
#    names = ['Alice', 'Bob', 'Charlie']
#    for name in names:
#        print("Hello, " + name + "!")
#
#28. How can you use an if statement within a for loop to 
#print even numbers from a given range?
#    a)
#    for i in range(10):
#        if i % 2 == 0:
#            print(i)
#