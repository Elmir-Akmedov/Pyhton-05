"""
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

#C. Write a program to display each character from a string and if a 
#character is number then stop the loop.
#D. Write a program to calculate the sum of series up to n term. For example, 
#if n=5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
#E. Create a program that prompts the user to enter a number, 
#then use a while loop to count from 1 up to the user's number.
#F. Write a Python program that uses a while loop to print numbers from 1 to 10.
#G. Write a program that checks if a user-entered string is a palindrome (reads the same forwards 
#and backwards) using a while loop. Ignore spaces and letter case.
#H. Write a program that asks the user for an integer. If the number is even, divide it by 2, 
#if it's odd, multiply it by 3 and add 1. Repeat this process with the result until the result 
#becomes 1, and count how many steps it took.
#I. Create a program that calculates the sum of all even numbers from 1 to a user-specified 
#number using a while loop.
#J. Create a program that takes a list of numbers as input and reverses the list using a while loop. 
#Do this without using any built-in list reversal methods.
#
#- Extra Hard -
#Task A. Count the total number of digits in a number. If user enters 547,
#the program should add each digit, so the output is 16 (as 5 + 4 + 7 = 16).
#Task B. Write a program to display all prime numbers within a range.
#Task C. Create a program that takes a string as input and uses a while loop to reverse 
#and print the characters of the string.
#Task D. Write a program that checks if a user-entered string is a palindrome (reads the 
#same forwards and backwards) using a while loop. Ignore spaces and letter case.
#Task E. Develop a program that takes an integer as input and prints a number pyramid using a 
#while loop. For example, if the user enters 5, the program should print:
#    1
#   121
#  12321
# 1234321
#123454321
#
#- Chat GPT's Homework -
#Task 1: Countdown Timer
#Write a program that uses a while loop to create a countdown timer. 
#Ask the user to enter a number of seconds, and then display a countdown 
#from that number down to 0.
#
#Task 2: Number Guessing Game
#Create a number guessing game where the computer generates a random number, 
#and the user has to guess it. Use a while loop to allow the user to keep 
#guessing until they correctly guess the number.
#
#Task 3: Factorial Calculator
#Write a program that calculates the factorial of a given number using a while 
#loop. Ask the user for an integer input and compute its factorial.
#
#Task 4: Password Validation
#Implement a program that asks the user to enter a password. Use a while loop 
#to keep asking for the password until it matches a predefined correct password.
#
#Task 6: Sum of Even Numbers
#Calculate and display the sum of all even numbers from 1 to a user-defined 
#upper limit using a while loop.
#
#Task 7: Multiplication Table
#Generate and display the multiplication table for a given number using a while 
#loop. Ask the user for the number and the range (e.g., 1 to 10).
#
#Task 8: Pattern Printing
#Write a program that uses a while loop to print a pattern of asterisks, 
#where the number of asterisks on each line is equal to the line number. 
#For example:
#*
#**
#***
#****
#*****
#
#Task 9: Task with a for loop
#Create a program that uses both while and for loops. Ask the user for a number 
#and print its multiplication table using a for loop inside the while loop. 
#Continue asking for numbers until the user enters '0' to exit.
#
#Quiz.
#1. What is the primary purpose of a while loop in Python?
#    a) To execute a block of code a specific number of times.
#    b) To execute a block of code indefinitely.
#    c) To repeatedly execute a block of code as long as a specified condition remains true.
#    d) To execute a block of code only once.
#
#2. What are some best practices for using while loops in Python?
#    a) Always initialize loop control variables within the loop.
#    b) Use vague variable names to encourage creativity.
#    c) Avoid ensuring the loop condition will eventually become false.
#    d) Use meaningful variable names and prevent infinite loops.
#
#3. What should you consider when using a while loop in Python?
#    a) Potential performance impact.
#    b) Using while loops for known iterations.
#    c) Never managing loop control variables.
#    d) Using while loops for all types of iterations.
#
#4. What are the key differences between while and for loops in Python?
#    a) While loops are primarily used for iteration, while for loops are used 
#    for conditional execution.
#    b) While loops are preferred when you know the number of iterations in advance.
#    c) For loops require manual management of the loop control variable and condition.
#    d) For loops are more flexible and can handle dynamic conditions, while 
#    while loops are used for iterating over sequences.
#
#5. What is the potential risk of using an infinite while loop in your code?
#    a) It can improve code performance.
#    b) It can lead to unexpected program termination.
#    c) It's a best practice for certain situations.
#    d) It simplifies code readability.
#
#6. How do you ensure that a while loop will terminate and not result in an infinite loop?
#    a) By not using while loops at all.
#    b) By initializing loop control variables within the loop.
#    c) By ensuring the loop condition becomes false at some point.
#    d) By using a try-except block.
#
#7. Which of the following statements is true about the loop control variable in a while loop?
#    a) It should always be initialized within the loop.
#    b) It should be set to any random value before entering the loop.
#    c) It is used to define the loop condition and manage loop execution.
#    d) It is optional and not required for a while loop.
#
#8. In Python, what happens when the condition of a while loop is initially False?
#    a) The loop is skipped entirely, and the code continues after the loop.
#    b) An error is raised.
#    c) The loop executes at least once.
#    d) The loop runs indefinitely.
#
#9. What is an off-by-one error in the context of while loops?
#    a) An error that occurs when the loop control variable is not properly initialized.
#    b) An error that happens when a loop runs one more or one less time than intended.
#    c) An error that occurs when the loop condition is too complex.
#    d) An error that occurs when using for loops instead of while loops.
#
#10. What is the output of the following code?
#    count = 1
#    while count <= 5:
#        print(count)
#        count += 1
#
#    a) 1 2 3 4 5
#    b) 1 2 3 4
#    c) 1 2 3 4 5 6
#    d) 2 3 4 5
#
#11. What is the output of the following code?
#    while True:
#        print("Infinite Loop")
#
#    a) Infinite Loop
#    b) Nothing (The loop will run indefinitely)
#    c) Error
#    d) None of the above
#
#12. What is the output of the following code?
#    count = 1
#    while count <= 10:
#        if count == 5:
#            break
#        print(count)
#        count += 1
#
#    a) 1 2 3 4 5 6 7 8 9 10
#    b) 1 2 3 4
#    c) 5 6 7 8 9 10
#    d) 1 2 3 4 6 7 8 9 10
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
#    b) 1 3 5
#    c) 2 4
#    d) 1 2 4
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
#    a) 1 1 2 1 3 1
#    b) 1 1 2 1 3 2
#    c) 1 2 2 2 3 1
#    d) 1 2 2 1 3 2
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
#    b) 30
#    c) 720
#    d) 25
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
#    a) The program adds numbers until the user enters 0 and then displays the sum.
#    b) The program keeps asking for numbers indefinitely.
#    c) The program calculates the factorial of the entered number.
#    d) The program displays an error message.
#
#17. What is the value of x:
#    x = 0
#    while (x < 100):
#        x += 2
#        print(x)
#
#    a) 101
#    b) 99
#    c) None of the above, this is an infinite loop
#    d) 100
#
#18. What is the output of the following if statement
#    a, b = 12, 5
#    if a + b:
#        print('True')
#    else:
#        print('False')
#
#    a) False
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
#    a) 20
#    b) 21
#    c) 10
#    d) 30
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
#    b)
#    11
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
#    b) 
#    10 Chair
#    10 Table
#"""