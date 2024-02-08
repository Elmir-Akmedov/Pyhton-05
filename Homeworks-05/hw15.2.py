"""
#- For Loops -
#A. Write a Python program that uses a for loop to print 
#all even numbers from 1 to 20, inclusive. Use the continue 
#statement to skip odd numbers during the iteration.
for x in range(1, 20):
    if x % 2 == 0:
        print(x)

#B. Write a Python program that asks the user to input 10 numbers. 
#Use a for loop to iterate through the numbers. Print the sum of 
#all numbers entered by the user. Use the break statement to exit 
#the loop early if the user inputs a negative number.
print("Enter numbers:")
user_nums = []
for x in range(10):
    a = float(input(">> "))
    if a < 0:
        print("You can't enter negative nums!!!")
        break
    user_nums.append(a)

print(sum(user_nums))

#C. Write a Python program that takes an integer as input from 
#the user and prints its multiplication table up to 10 using a for loop. 
#Use the continue statement to skip the multiplication if the result 
#is less than 30.
user_num = int(input(">> "))
for x in range(1, 11):
    if (user_num * x) < 30:
        continue
    print(f"{user_num} x {x} = {user_num * x}")
    

#D. Write a Python program to find and print all prime numbers between 
#1 and 50 using a for loop. Use the break statement to exit the loop 
#early if a non-prime number is encountered.
import time
start = time.time()
a = range(1, 150000)
lst = []
lst1 = []
for x in a:
    for b in range(2, x//2):
        if x % b == 0:
            break
    else:
        lst1.append(x)
print(lst1)
end = time.time()
print(end - start)

#E. Write a Python program to generate and print the first 10 numbers 
#in the Fibonacci sequence using a for loop. Use the continue statement 
#to skip printing a number if it is greater than 100.
a = 0
b = 1
c = 0
for _ in range(12):
    print(c)
    a = b
    b = c
    c = a + b

#F. Write a Python program that asks the user to input an integer n. 
#Using a for loop, print all even numbers in reverse order from n down 
#to 2. Use the continue statement to skip odd numbers during the iteration.
n = int(input(">> "))
for x in range(n, 1, -1):
    if x % 2 != 0:
        continue
    print(x)

#G. Write a Python program that prompts the user for a password. Use a for 
#loop to iterate over a predefined list of passwords. If the entered password 
#matches any of the predefined passwords, print "Access granted" and use the 
#break statement to exit the loop. If no match is found, print "Access denied".
passwords = ["elmir", "elmir2", "elmir3", "elmir4","elmir5"]
print("Please enter password:")
password = input(">> ")
for x in passwords:
    if password == x:
        print("Access granted")
        break

#H. Write a Python program that asks the user to enter a series of numbers. 
#Use a for loop to iterate through the numbers. Compute and print the average 
#of all positive numbers entered by the user. Use the continue statement 
#to skip negative numbers during the calculation.
user_inputs = input(">> ").split()
nums_list = [int(x) for x in user_inputs]
formatted_nums = []

def remove_neqative(nums_list: list) -> list:
    for x in nums_list:
        if x < 0:
            continue
        formatted_nums.append(x)


def calculating_average(formatted_nums: list) -> float:
    average = sum(formatted_nums) / len(formatted_nums)
    return average


if __name__ == "__main__":
    remove_neqative(nums_list)
    average = calculating_average(formatted_nums)
    print(average)
    

#I. Write a Python program that prompts the user to input a sentence. 
#Use a for loop to iterate through the characters in the sentence and count 
#the number of vowels (a, e, i, o, u). Print the total count of vowels. 
#Use the continue statement to skip counting for non-alphabetic characters.

wovels = ("a", "e", "i", "o", "u")
user_input = input(">> ")
def count_wovels(user_input: str):
    wowels_amount = 0
    for x in user_input:
        if x in wovels:
            wowels_amount += 1
    return wowels_amount
    
        
if __name__ == "__main__":
    wowels_amount = count_wovels(user_input)
    print(wowels_amount)


#J. Write a Python program that generates a random password of a specified 
#length based on user input. Ask the user to input the desired password 
#length and use a for loop to generate and print the password. Use the 
#break statement to exit the loop after generating the password.

import string
from secrets import choice



user_input = int(input(">> "))


def create_password(password_len: int) -> str:
    password = ""
    for x in range(password_len):
        a = choice(string.ascii_letters)
        password += a 
    return password


password = create_password(user_input)
print(password)


#K. Write a Python program that prompts the user to enter the names of 
#three cities and their corresponding populations. Use a for loop to populate 
#a dictionary where the city names are keys and the populations are values.

city_population = {}

for i in range(3):
    city = input("Enter the name of a city: ")
    population = int(input(f"Enter the population of {city} : "))
    city_population[city] = population

print(city_population)

#L. Write a Python program that asks the user to input a sentence. Use a for 
#loop to iterate through the characters in the sentence and count the number 
#of vowels (a, e, i, o, u). Store the counts in a dictionary where the vowels 
#are keys and the counts are values.

wovels = ("a", "e", "i", "o", "u")
user_input = input(">> ")
def count_wovels(user_input: str) -> dict:
    wowels_amount_dict = {"a": 0,
                          "e": 0,
                          "i": 0,
                          "o": 0,
                          "u": 0
                          }
    for x in user_input:
        if x in wovels:
            wowels_amount_dict[x] += 1
    return wowels_amount_dict
    
        
if __name__ == "__main__":
    wowels_amount_dict = count_wovels(user_input)
    print(wowels_amount_dict)


#M. Write a Python program that allows the user to enter key-value pairs into 
#a dictionary. Prompt the user to input a key and a value, and use a for loop 
#to allow them to enter multiple pairs. Print the dictionary after each addition.

user_dictionary = {}

for i in range(3):
    key = input("Enter the name of your key: ")
    value = int(input(f"Enter the value of {key} : "))
    user_dictionary[key] = value
    print(user_dictionary)



#N. Write a Python program that prompts the user to input a word or phrase. 
#Use a for loop to iterate through the characters and count the frequency of 
#each letter in the input. Store the counts in a dictionary where the letters 
#are keys and the counts are values.
import string



user_input = input(">> ")

def count_letters(user_input: str) -> dict:
    letters_amount_dict = {}
    for x in user_input:
        if x not in string.ascii_letters:
            continue
        if x in letters_amount_dict:
            letters_amount_dict[x] += 1
        else:
            letters_amount_dict[x] = 1
    return letters_amount_dict
    
        
if __name__ == "__main__":
    letters_amount_dict = count_letters(user_input)
    print(letters_amount_dict)


#O. Write a program to use for loop to print the following reverse number pattern:
#5 4 3 2 1 
#4 3 2 1 
#3 2 1 
#2 1 
#1
user_input = int(input(">> "))
for x in range(user_input, 0, -1):
    for y in range(x):
        print(f"{x - y}", end=" ")
    print()
        

#P. Display numbers from -10 to -1 using for loop. The step of your range
#method should be positive, not negative. The output:
#-10
#-9
#-8
#-7
#-6
#-5
#-4
#-3
#-2
#-1

for x in reversed(range(1, 11)):
    print(f"-{x}")


#
#- EXTRA HARD -
#Task 1.
#Count the total number of digits in a number.
#Write a program to count the sum of digits in a number.
#For example, the number is 75869, so the output should be 35 (7 + 5 + 8 + 6 + 9).

user_input = input(">> ")

def count_digits(user_num):
    digits = [float(x) for x in user_num]
    digits_sum = sum(digits)
    print(digits_sum)


if __name__ == "__main__":
    count_digits(user_input)


#Task 2.
#Write a program to calculate the sum of series up to n term. 
#For example, if n = 5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
a = "2"
b = "2"
digits = []
for x in range(5):
    digits.append(int(b))
    b = b + a

digits_sum = sum(digits)
print(digits_sum)

#Task 3.
#Write a program to display whether the number is prime or not.
#Prime numbers are natural numbers that are divisible by only 1 and the number itself.

user_input = int(input(">> "))
if user_input % 2 == 0:
    print("Not prime num")
else:
    print("prime num")


#
#- Chat GPT's Project -
#Project: Password Validation
#
#Write a Python program that prompts the user to enter a password. The program 
#should check the validity of the password based on the following conditions:
#
#The password must be at least 8 characters long.
#The password must contain at least one uppercase letter, one lowercase letter, 
#and one numeric digit.
#The password must not contain the word "password" (case insensitive).
#Use a for loop to iterate through the characters of the password and implement 
#the following actions:
#
#If the current character is a space, use continue to skip the rest of the loop 
#and move to the next character.
#If the password contains the word "password" (case insensitive), use break to 
#immediately exit the loop and print "Invalid password".
#After the loop, check if the password meets all the conditions. If it does, 
#print "Valid password". Otherwise, print "Invalid password".
#Ensure that the program provides appropriate messages to guide the user and 
#thoroughly tests the input for validity.
#
#This task challenges the usage of for loops, break, and continue to handle 
#complex conditions and ensure secure password validation. Happy coding!

user_password = input(">> ")
password = [x for x in user_password]


def check_len():
    if len(user_password) < 8:
        exit("The password must be at least 8 characters long.")
    elif user_password == "password":
        exit("The password must not contain the word \"password\"")
    return True


def has_uppercase():
    for x in password:
        if x.isupper():
            return True
    return False


def has_lowercase():
    for x in password:
        if x.islower():
            return True
    return False


def has_digit():
    for x in password:
        if x.isdigit():
            return True
    return False


def password_validation():
    if (check_len()
        and has_digit()
         and has_uppercase()
           and has_lowercase()
             ):
        print("Valid password")
    else:
        print("Invalid password")

password_validation()
"""
#
#Quiz.
#1. What is the purpose of the continue statement in a for loop?
#    b) It skips the rest of the loop and moves to the next iteration.
#
#2. In a for loop, the break statement is used to:
#    b) Exit the loop and move to the next block of code.
#
#3. Which of the following statements is true about the for loop in Python?
#    c) The loop variable is optional.
#
#4. For the following code snippet, determine the output or the result of the operation:
#    numbers = [1, 2, 3, 4, 5]
#    total = 0
#    for num in numbers:
#        if num % 2 == 0:
#            total += num
#        else:
#            continue
#    print(total)
#    Result: 6
#
#5. For the following code snippet, determine the output or the result of the operation:
#    numbers = [10, 20, 30, 40, 50]
#    total = 0
#    for num in numbers:
#        if num > 30:
#            break
#        if num % 2 == 0:
#            total += num
#        else:
#            continue
#    print(total)
#    Result: 30
#
#6. What is the value of the var after the for loop completes its execution:
#    var = 10
#    for i in range(10):
#        for j in range(2, 10, 1):
#            if var % 2 == 0:
#                continue
#                var += 1
#        var += 1
#    else:
#        var += 1
#    print(var)
#
#    b) 21
#
#7. What is the output of the following range() function:
#    for num in range(2,-5,-1):
#        print(num, end=", ")
#
#    c) 2, 1, 0, -1, -2, -3, -4
#
#8. What is the value of x after the following nested for loop completes its execution:
#    x = 0
#    for i in range(10):
#        for j in range(-1, -10, -1):
#            x += 1
#            print(x)
#    
#    b) 90
#
#9. What is the output of the following nested loop?
#    for num in range(10, 14):
#        for i in range(2, num):
#            if num % i == 1:
#                print(num)
#                break
#     output: 11,12,13            
#10. What is the output of the following nested loop?
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
#
#11. What is the output of the following loop?
#    for l in 'Jhon':
#        if l == 'o':
#            pass
#        print(l, end=", ")
#            
#    a) J, h, n,
#
#- True or False -
#True or False: A for loop in Python can be nested within another for loop.
True
#True or False: The continue statement is used to immediately exit the loop
#and terminate the program.
True
#True or False: The break statement is used to exit the loop prematurely, 
#regardless of whether the loop condition is met.
True
#True or False: The break statement is used to skip the rest of the loop and 
#move to the next iteration.
False
#True or False: The continue statement is used to exit the loop prematurely, 
#regardless of whether the loop condition is met.
False
#True or False: Using break is more appropriate when you want to exit the 
#loop prematurely based on a certain condition, regardless of whether the 
#loop has completed all iterations. It allows you to terminate the loop early 
#and continue with the rest of the program.
True
#True or False: Using continue is more appropriate when you want to skip the 
#current iteration and proceed to the next iteration based on a certain condition, 
#but you still want to continue the loop.
True


