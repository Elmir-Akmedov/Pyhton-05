"""
- For Loops -
A. Write a program to use the loop to find the factorial of a given number.
B. Write a program that uses a for loop to print numbers from 1 to 10. However, 
if the number is divisible by 3, skip the loop, and if the number is 7, stop the loop.
C. In Python, what is the purpose of the range() function when used with a for loop?
D. How can you prematurely exit a for loop in Python?
E. What is an iterator in Python, and how is it related to for loops?
F. How can you iterate through the elements of a list in reverse order using a for loop?
G. Create a for loop that prints all even numbers from 20 to 40. Solve this task in
two different ways (modifying range() and using if-statements).
H. Write a for loop to calculate the sum of all integers from 1 to 100. At the end of the loop 
the program should print 'The end of a task.'
I. Generate a multiplication table for a given number using a for loop, e.g., for the number 5, print 5x1, 5x2, ..., 5x10.
J. Write a for loop to iterate through a string and print each character on a separate line
with corresponding index.
K. Suppose you have the following list:
employees = ["Bob", "John", "Brad", "Jake", "Michael", "Jim"]

Iterate over this list and print all names except the ones which start with the
letter 'J'.
L. Suppose you have the following list:
stock = ["Cherry", "Lemon", "Watermelon", "Carrot", "Banana", "Coconut", "Pumpkin", "Apple", "Grape", "Cucumber"]

Iterate over this list and print all fruits and vegetables except the ones which start with the
letter 'C' and whichs length is less than or equal 6.
M. Write a for loop to reverse a given string. For example, "hello" should become 'olleh'.
You shouldn't use any reversing methods such as [::-1]. Instead you should make manipulations
with string literals.
N. Write a for loop to check and print all prime numbers within a given range (on dynamic user input).
O. Implement a for loop to search for a specific word in a text and replace it with another word.
P. Write a program that draws the pyramid as:
Reverse Pyramid
  ***********     
   *********
    *******
     *****
      ***
       *
Q. Write the shortest program that prints the position and each character of a string.
print([f"{x}:{"Elmir"[x]}" for x in range(len(Elmir)])
R. You have the following dictionary:
data = {
    "key1": 80,
    "key2": 75,
    "key3": 65,
    "key4": 85
}

Iterate over it and check if any value is less than 80, add the missing points.
S. Copy this code to your file:
from random import randint
numbers = [randint(15, 40) for _ in range(5)]

This gives you a list of 5 random numbers between 15 and 40. Using for loops
find the max value of that list, and print the list to see values.
T. Use 'numbers' list from Task S. Iterate over it again, and if there is a number
between 20 and 25 exit the loop, otherwise print the value.
U. Write a Python program to construct the following pattern:
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
V. Write a Python program to count the number of even and odd numbers in a collection of numbers.
W. Write a Python program that prints each item and its corresponding type from the following list.
[5, True, "Python", (1, 2, 3), [5, 6, 7], 9.99, {"name":"Mark"}]
X. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
Y. Write a Python program that accepts a string and calculates the number of digits and letters.
Z. Write a Python program to guess a number between 1 and 9. The program should use 'random' module,
give only 3 chances to guess the number. Print 'Congratulations' if you guess and 'Game Over'
if you fail.

- Chat GPT's Homework -
Problem 1: Generate a Series
Write a Python program that uses a for loop to generate and print the following 
series of numbers: 1, 4, 9, 16, 25, ... up to a given positive integer n. The 
series consists of perfect squares.

Problem 2: Calculate Factorial with a For Loop
Write a Python program that calculates the factorial of a given positive integer n 
using a for loop. Display the result.

Problem 3: Password Generator
Write a Python program that generates a random password consisting of both uppercase 
and lowercase letters, digits, and special characters. The password should be of a 
specified length n. Use a for loop to create the password.

Problem 4: Average of Numbers
Write a Python program that calculates the average of a list of numbers using a 
for loop. Prompt the user to enter a list of numbers (comma-separated), and then 
compute and display the average.

Problem 5: Pattern Printing
Write a Python program that prints the following pattern using nested for loops:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

Problem 6: Count Vowels and Consonants
Write a Python program that counts the number of vowels and consonants in a given 
string. Use a for loop to iterate through the characters of the string and 
categorize them as vowels or consonants. Display the counts separately.

Problem 7: Reverse a List
Write a Python program that takes a list as input and uses a for loop to reverse 
the order of elements in the list. Display the reversed list.

Problem 8: Finding Factors
Write a Python program that prompts the user to enter a positive integer and 
then finds and prints all the factors of that integer using a for loop.

Quiz.
1. How do you terminate a 'for' loop prematurely in Python?
    a) Using 'break'
    b) Using 'continue'
    c) Using 'return'

2. What is the syntax for a 'for' loop in Python?",
    a. for (var i = 0; i < 5; i++)
    b. for i in range(5)
    c. while i < 5

3. Which statement is used to skip the current iteration and continue to the next 
in a 'for' loop?
    a) 'pass'
    b) 'break'
    c) 'continue'

4. What is the maximum number of times a 'for' loop can iterate?",
    a) 100
    b) 1000
    c) It depends on the specific code
    d) There is no maximum limit

5. Which data types can be iterated over using a 'for' loop in Python?
    a) Lists and tuples 
    b) Lists and dictionaries
    c) Dictionaries and sets

6. In a 'for' loop, how can you access both the index and value of each element in a list?
    a) Use a while loop instead 
    b) Use the enumerate() function
    c) Manually calculate the index
"""