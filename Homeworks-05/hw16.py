"""

#- While Loops -
#A. Write a program that asks user for a number between 100 and 500. The program should ask the user
#until he/she enters the number within a given range.
print("Please enter a number between 100 and 500:")

while True:
    user_input = float(input(">> "))
    if 100 < user_input < 500:
        print("Thanks")
        break
    else:
        print("Try again")

#B. Write a program that prints even and odd numbers between 1 to the entered number.
print("Enter any number you want:")
user_input = int(input(">> "))
even_nums = []
odd_nums = []

for x in range(1, user_input):
    if x % 2 == 0:
        even_nums.append(x)
    else:
        odd_nums.append(x)

print(f"Even nums: {even_nums}")
print(f"Odd nums: {odd_nums}")

#C. Write a program to display each character from a string and if a 
#character is number then stop the loop.
string = "Elmir2Seymur"
for x in string:
    if x.isdigit():
        print(x)
        break
    print(x)

#D. Write a program to calculate the sum of series up to n term. For example, 
#if n=5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
a = "2"
b = "2"
digits = []
for x in range(5):
    digits.append(int(b))
    b = b + a

digits_sum = sum(digits)
print(digits_sum)


#E. Create a program that prompts the user to enter a number, 
#then use a while loop to count from 1 up to the user's number.
user_input = int(input(">> "))
for x in range(1, user_input + 1):
    print(x, end=",")

#F. Write a Python program that uses a while loop to print numbers from 1 to 10.
num = 1
while num <= 10:
    print(num)
    num += 1

#G. Write a program that checks if a user-entered string is a palindrome (reads the same forwards 
#and backwards) using a while loop. Ignore spaces and letter case.
user_input = input(">> ").lower().replace(" ", "")
start = 0
end = len(user_input) - 1

while True:
    if user_input[start] == user_input[end]:
        print("Polindrom")
        break
    start += 1
    end -= 1
    if start > end:
        print("Not polindrom")
        break


#H. Write a program that asks the user for an integer. If the number is even, divide it by 2, 
#if it's odd, multiply it by 3 and add 1. Repeat this process with the result until the result 
#becomes 1, and count how many steps it took.

user_input = (int(input(">> ")))
steps = 0
while user_input != 1:
    if user_input % 2 == 0:
        user_input = user_input / 2
    else:
        user_input = (user_input * 3) + 1
    steps += 1
print(steps)


#I. Create a program that calculates the sum of all even numbers from 1 to a user-specified 
#number using a while loop.

user_input = int(input(">> "))
x = 0
a = 0
while x != user_input + 1:
    sum = a + x
    a += x
    x += 1
print(sum)


#J. Create a program that takes a list of numbers as input and reverses the list using a while loop. 
#Do this without using any built-in list reversal methods.

user_input = input(">> ").split()
end = len(user_input) - 1
while end != -1:
    print(user_input[end], end=",")
    end -= 1

  
#
#- Extra Hard -
#Task A. Count the total number of digits in a number. If user enters 547,
#the program should add each digit, so the output is 16 (as 5 + 4 + 7 = 16).

user_input = input(">> ")

def count_digits(user_num):
    digits = [float(x) for x in user_num]
    digits_sum = sum(digits)
    print(digits_sum)


if __name__ == "__main__":
    count_digits(user_input)

#Task B. Write a program to display all prime numbers within a range.
user_input = int(input(">> "))
prime_nums = []
for num in range(2, user_input + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_nums.append(num)
print(prime_nums)


#Task C. Create a program that takes a string as input and uses a while loop to reverse 
#and print the characters of the string.

user_input = input(">> ")
end = len(user_input) - 1
while end != -1:
    print(user_input[end], end=",")
    end -= 1
 
#Task D. Write a program that checks if a user-entered string is a palindrome (reads the 
#same forwards and backwards) using a while loop. Ignore spaces and letter case.

user_input = input(">> ").lower().replace(" ", "")
start = 0
end = len(user_input) - 1

while True:
    if user_input[start] == user_input[end]:
        print("Polindrom")
        break
    start += 1
    end -= 1
    if start > end:
        print("Not polindrom")
        break

#Task E. Develop a program that takes an integer as input and prints a number pyramid using a 
#while loop. For example, if the user enters 5, the program should print:
#    1
#   121
#  12321
# 1234321
#123454321
user_input = int(input(">> ")) 
x = 1

while x <= user_input:
    spaces = " " * (user_input - x)
    numbers = ""
    for i in range(1, x + 1):
        numbers += str(i)
    for j in range(x - 1, 0, -1):
        numbers += str(j)
    print(spaces + numbers)
    x += 1

#- Chat GPT's Homework -
#Task 1: Countdown Timer
#Write a program that uses a while loop to create a countdown timer. 
#Ask the user to enter a number of seconds, and then display a countdown 
#from that number down to 0.
import time
import os



start = int(input(""))
while start >= 0:
    print(start)
    time.sleep(1)
    os.system("cls")
    start -= 1


#Task 2: Number Guessing Game
#Create a number guessing game where the computer generates a random number, 
#and the user has to guess it. Use a while loop to allow the user to keep 
#guessing until they correctly guess the number.
import random

random_num = random.randint(1, 3)

while True:
    user_input = int(input(">> "))
    if random_num == user_input:
        print("correct")
        break
    else:
        print("Wrong")



#Task 3: Factorial Calculator
#Write a program that calculates the factorial of a given number using a while 
#loop. Ask the user for an integer input and compute its factorial.
user_input = int(input(">> "))
x = 2
c = 1
while x <= user_input:
    c = c * x
    x += 1
    
print(c)

#Task 4: Password Validation
#Implement a program that asks the user to enter a password. Use a while loop 
#to keep asking for the password until it matches a predefined correct password.


passwords = ["elmir", "elmir2", "elmir3", "elmir4","elmir5"]
print("Please enter password:")
password = input(">> ")
while True:
    if password in passwords:
        print("Correct")
        break

#Task 6: Sum of Even Numbers
#Calculate and display the sum of all even numbers from 1 to a user-defined 
#upper limit using a while loop.

user_input = int(input(">> "))
x = 1
even_nums = []
while x <= user_input:
    if x % 2 == 0:
        even_nums.append(x)
    x += 1
print(sum(even_nums))



#Task 7: Multiplication Table
#Generate and display the multiplication table for a given number using a while 
#loop. Ask the user for the number and the range (e.g., 1 to 10).
user_input = int(input(">> "))
start = int(input(">> "))
end = int(input(">> "))

while start <= end:
    result = user_input * start
    print(f"{user_input} * {start} = {result}")
    start += 1

#Task 8: Pattern Printing
#Write a program that uses a while loop to print a pattern of asterisks, 
#where the number of asterisks on each line is equal to the line number. 
#For example:
#*
#**
#***
#****
#*****

user_input = int(input(">> "))
n = 1
while n <= user_input:
    stars = "*" * n
    print(stars)
    n += 1

#Task 9: Task with a for loop
#Create a program that uses both while and for loops. Ask the user for a number 
#and print its multiplication table using a for loop inside the while loop. 
#Continue asking for numbers until the user enters '0' to exit.

while True:
    user_input = int(input(">> "))
    start = int(input(">> "))
    end = int(input(">> "))
    for x in range(end):
        result = user_input * start
        print(f"{user_input} * {start} = {result}")
        start += 1
    if user_input == 0:
        break
"""
#Quiz.
#1. What is the primary purpose of a while loop in Python?
#    c) To repeatedly execute a block of code as long as a specified condition remains true.
#
#2. What are some best practices for using while loops in Python?
#    d) Use meaningful variable names and prevent infinite loops.
#
#3. What should you consider when using a while loop in Python?
#    a) Potential performance impact.
#
#4. What are the key differences between while and for loops in Python?
#    b) While loops are preferred when you know the number of iterations in advance.
#
#5. What is the potential risk of using an infinite while loop in your code?
#    b) It can lead to unexpected program termination.
#
#6. How do you ensure that a while loop will terminate and not result in an infinite loop?
#    c) By ensuring the loop condition becomes false at some point.
#
#7. Which of the following statements is true about the loop control variable in a while loop?
#    c) It is used to define the loop condition and manage loop execution.
#
#8. In Python, what happens when the condition of a while loop is initially False?
#    a) The loop is skipped entirely, and the code continues after the loop.
#
#9. What is an off-by-one error in the context of while loops?
#    a) An error that occurs when the loop control variable is not properly initialized.
#
#10. What is the output of the following code?
#    count = 1
#    while count <= 5:
#        print(count)
#        count += 1
#
#    a) 1 2 3 4 5
#
#11. What is the output of the following code?
#    while True:
#        print("Infinite Loop")
#
#    b) Nothing (The loop will run indefinitely)
#
#12. What is the output of the following code?
#    count = 1
#    while count <= 10:
#        if count == 5:
#            break
#        print(count)
#        count += 1
#
#    b) 1 2 3 4
#
#13. What is the output of the following code?
#    count = 1
#    while count <= 5:
#        if count % 2 == 0:
#            count += 1
#            continue
#        print(count)
#        count += 1
#
#    a) 1 2 3 4 5
#
#14. What is the output of the following code?
#    outer_count = 1
#    while outer_count <= 3:
#        inner_count = 1
#        while inner_count <= 2:
#            print(outer_count, inner_count)
#            inner_count += 1
#        outer_count += 1
#
#    e) None of the above
#
#15. What is the output of the following code?
#    num = 5
#    fact = 1
#    while num > 0:
#        fact *= num
#        num -= 1
#    print(fact)
#
#    a) 120
#
#16. What is the output of the following code?
#    total = 0
#    while True:
#        num = int(input("Enter a number (0 to exit): "))
#        if num == 0:
#            break
#        total += num
#    print("Sum:", total)
#
#    a) The program adds numbers until the user enters 0 and then displays the sum..
#
#17. What is the value of x:
#    x = 0
#    while (x < 100):
#        x += 2
#        print(x)
#
#    d) 100
#
#18. What is the output of the following if statement
#    a, b = 12, 5
#    if a + b:
#        print('True')
#    else:
#        print('False')
#
#    b) True
#
#19. What is the value of the var after the for loop completes its execution:
#    var = 10
#    for i in range(10):
#        for j in range(2, 10, 1):
#            if var % 2 == 0:
#                continue
#                var += 1
#        var+=1
#    else:
#        var+=1
#
#    b) 21
#
#20. What is the output of the following nested loop:
#    for num in range(10, 14):
#        for i in range(2, num):
#            if num%i == 1:
#                print(num)
#                break
#
#    a)
#    10
#    11
#    12
#    13
#
#21. What is the output of the following nested loop:
#    numbers = [10, 20]
#    items = ["Chair", "Table"]
#
#    for x in numbers:
#        for y in items:
#            print(x, y)
#
#    a)
#    10 Chair
#    10 Table
#    20 Chair
#    20 Table
#"""
