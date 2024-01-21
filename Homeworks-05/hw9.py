"""
#Note. You should use indexing, negative indexing, slicing method,
#mathematical operations and other techniques to accomplish tasks.
#
#- Lists -
#A. Create a list containing minimum seven different colors.
colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Black"]

#B. Create a list containing minimum five different countries.
countries = ["U.S", "France", "Japan", "Australia", "Brazil"]

#C. Create a list containing three string values and two integer values.
list = ["apple", "banana", "orange", 19, 30]

#D. Create a list containing all continents of the world.
continents = ["Africa", "Antarctica", "Asia", "Europe", "North America", "Australia", "South America"]

#E. Create a list containing minimum four car brands.
car_brands = ["Dodge", "Ford", "BMW", "Hyundai"]

#F. Create a list containing four different data types of Python.
data_types = ["Hello", 42, 3.14, True]

#G. Create a list containing only negative even numbers from -2 to -12.
negative_even_numbers = [-2, -4, -6, -8, -10, -12]

#H. Create a list containing only positive even numbers from 0 to 12.
positive_even_numbers = [2, 4, 6, 8, 10, 12]

#I. Combine lists from Task G and H.
combined_lists = [-12, -10, -8, -6, -4, -2, 2, 4, 6, 8, 10, 12]

#J. Create a list containing minimum six students' names. Print the first student's name.
students = ["Elmir", "Seymur", "Eli", "Ayxan", "Suphan", "Elcan"]
print(students[0])

#K. Create a list containing three different integers. Print the integer at position two.
integers = [5, 10, 15]
print(integers[1])

#L. Print the last element of Task D's list.
print(continents[-1])

#M. Print the last 2 elements of Task A's list. You can use slicing method only once. Separately printing those elements will not be accepted.
print(colors[-2:])

#N. Given the following list: three = [3, 3, 3] Create a new list containing the triple value of that list.
three = [3, 3, 3]
new_list = three * 3

#O. Create any nested list. Print any value from the inner list and the whole inner list.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[0][1]) #Value from the inner list
print(nested_list[0]) #Whole inner list

#P. Change the value of the color at position six of the list from Task A.
colors[5] = "White"

#Q. From Task B's list print all countries except the first two.
print(countries[2:])

#R. Create two new lists containing the double value of the list from Task F using 2 different mathematical operations (methods).
multiply_metod = [value * 2 for value in data_types]
addition_metod = [value + value for value in data_types]
print(multiply_metod)
print(addition_metod)

#S. From the following list change the value of the last element to "Bob":friends = ["Kevin", "Karen", "Jim", "Carry"]
friends = ["Kevin", "Karen", "Jim", "Carry"]
friends[-1] = "Bob"

#T. Create an empty list.
empty_list = []
#
#- Interview Question -
#A. Reverse a list with slicing method.
reversed_list = colors[::-1]
#
#Bonus:
#A. Print the whole list from previous tasks using the slicing method.
#B. Print the length of any list from previous tasks.
list_lenght = len(colors)


#
#

#Note. Add the following list at the top of your code. You will use this list
#during the homework in certain tasks:
fruits = ["Apple", "Banana", "Orange", "Grape", "Strawberry", "Kiwi", "Cherry"]

#Also print the list's modification versions to see the difference.
#- List Methods -
#A. Make up a formula with built-in python 'len' method that finds helps to get the last element from the 'fruits' list.
last_fruit = fruits[len(fruits) - 1]
print(last_fruit)

#B. Add any two fruits to the 'fruits' list.
fruits.append("Mango")
fruits.append("Pineapple")
print(fruits)
#C. Remove third fruit so you can assign it to a variable.
removed_fruit = fruits.pop(2)
print(removed_fruit)
print(fruits)

#D. Add a fruit to the 'fruits' list twice, and then print the amount of  this fruit in the 'fruits' list.
fruits.append("Apple")
fruits.append("Apple")
count_of_fruit = fruits.count("Apple")
print(f"Count of \"Apple\": {count_of_fruit}")
print(fruits)

#E. Find the index of 'Grape' object in the 'fruits' list.
grape_index = fruits.index("Grape")

#F. Add 'Avocado' to the 'fruits' list at position four. 
fruits.insert(3, "Avocado")

#G. Remove third fruit without getting the removed fruit.
fruits.pop(2)

#H. Remove a fruit at position one.
fruits.pop(1)

#I. Add 'Blackberry' to the end of the 'fruits' list. Remove it using 'pop'  method by finding its positive index.
fruits.append("Blackberry")
blackberry_index = fruits.index("Blackberry")
fruits.pop(blackberry_index)

#J. Reverse the 'fruits' list with two different methods. Each time print  the reversed list.
fruits1 = fruits.copy()  # Create a copy to preserve the original list
fruits1.reverse()
print(fruits1)
fruits2 = fruits[::-1]
print(fruits2)

#K. Sort alphabetically the 'fruits' list. Print the sorted version of the  list.
fruits.sort()
print(fruits)

#L. Suppose you have the following list:Extend the 'fruits' list with the new list.
new_fruits = ["Papaya", "Lime", "Lemon", "Peach"]
fruits.extend(new_fruits)

#M. Make a copy of the 'fruits' list. Remove the last three fruits. Print  both of the lists ('fruits' and the modified copied version).
fruits_copy = fruits.copy()
modified_fruits = fruits_copy[-3:]
print(fruits)
print(modified_fruits)

#N. Create a variable named 'occurrence'. Make it equal True if the 'Papaya' is in the 'fruits' list, otherwise False.
occurrence = "Papaya" in fruits
print(occurrence)

#O. Clear the 'fruits' list.
fruits.clear()
#
#- Variables -
#A. Suppose you have the following variables: x = 60, y = 70. You need to swap these variables values in one line of code.
x = 60
y = 70.
x, y == y, x

#- ChatGPT's homework (List Methods) -
#1. Append and Extend:
#a. Write a Python program that creates an empty list and then appends  the following elements to it: 10, 20, 30, 40, and 50. Print the list  after each append operation.
my_list = []
my_list.append(10)
print(my_list)
my_list.append(20)
print(my_list)
my_list.append(30)
print(my_list)
my_list.append(40)
print(my_list)
my_list.append(50)
print(my_list)

#b. Create a second list containing elements [60, 70, 80]. Extend the  first list using this second list and print the updated list.
second_list = [60, 70, 80]
my_list.extend(second_list)
print(my_list)

#2. Insert and Remove:
#a. Write a Python program that creates a list containing the following  elements: 'apple', 'banana', 'orange', 'grape', 'apple', 'kiwi'.
fruits = ['apple', 'banana', 'orange', 'grape', 'apple', 'kiwi']
print(fruits)

#b. Use the 'insert' method to add 'pear' between 'banana' and 'orange'  in the list. Print the updated list.
fruits.insert(2, 'pear')
print(fruits)

#c. Use the 'remove' method to remove the first occurrence of 'apple' from  the list. Print the updated list.
fruits.remove('apple')
print(fruits)

#3. Count and Index:
#a. Create a list containing the following elements: 2, 4, 6, 8, 4, 10, 4, 12, 14.
numbers = [2, 4, 6, 8, 4, 10, 4, 12, 14]

#b. Use the 'count' method to find how many times the number 4 appears in the list and print the count.
num_4 = numbers.count(4)
print(num_4)

#c. Use the 'index' method to find the index of the first occurrence of 4 in the list and print the index.
index_4 = numbers.index(4)
print(index_4)

#
#4. Sort and Reverse:
#a. Create a list containing the following integers in random order: 45, 23, 78, 12, 98, 56.
numbers = [45, 23, 78, 12, 98, 56]

#b. Use the 'sort' method to sort the list in ascending order and print the sorted list.
numbers.sort()
print(numbers)

#c. Use the 'reverse' method to reverse the sorted list and print the reversed list.
numbers.reverse()
print(numbers)

#
#5. Slice and Concatenate:
#a. Create a list containing the following elements: 'red', 'blue', 'green', 'yellow', 'orange', 'purple'.
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']
 
#b. Use slicing to extract a new list that contains only the first three colors. Print the new list.
first_three_colors = colors[:3]
print(first_three_colors)

#c. Use slicing again to extract a new list that contains the last three colors. Print the new list.
last_three_colors = colors[-3:]
print(last_three_colors)

#d. Concatenate the two sliced lists and print the final combined list.
combined_list = first_three_colors + last_three_colors
print(combined_list)

#
#
#

#- Lists -
#A. Create an empty list and add 5 user-input integers to it.
empty_list = []
user_input1 = int(input()) 
user_input2 = int(input()) 
user_input3 = int(input()) 
user_input4 = int(input()) 
user_input5 = int(input()) 
empty_list.append(user_input1)
empty_list.append(user_input2)
empty_list.append(user_input3)
empty_list.append(user_input4)
empty_list.append(user_input5)

#B. Take a list of integers as input and print the sum of all the elements in the list.
user_input = map(int, input("Enter the integers separated by space: ").split())
user_input_list = list(user_input)
sum_elements = sum(user_input_list)
print(sum_elements)

#C. Ask the user for a sentence and store each word as an element in a list.
user_input = map(str, input("Enter the sentence: ").split())
user_input_list = list(user_input)

#D. Write a program that asks user for six countries. The program should create a list of those countries and ask for three countries to delete from the list. Make the program user-friendly, and print each time the content of a list to show the user which countries are in a list.
countries = [input(f"Enter country {x + 1}:\n>> ") for x in range(6)]
print(f"This is your list:{countries}")
remove_countries = [input(f"Enter country {n + 1} for deleting:\n>> ") for n in range(3)]
countries.remove(remove_countries[0])
print(f"{remove_countries[0]} removed from your list.")
countries.remove(remove_countries[1])
print(f"{remove_countries[1]} removed from your list.")
countries.remove(remove_countries[2])
print(f"{remove_countries[2]} removed from your list.")
print(f"Your current list is:{countries}")

#E. Which list method makes any list look the same. The lists are the same if its content, elements and all other properties are the same.
#sort method

#F. Create an empty list and print its length.Write a function that accepts a list of names and returns the name with the longest length.
my_list = []
print(len(my_list))
my_list.append(list(input("Please enter a list opf names:\n>> ")))
print(f"Your longest lenght name is:{max(my_list, key=len)}")

#G. Ask the user for a list of integers and find the second-largest number in the list.
lenght_numbers_list = int(input("Please enter the lenght of your numbers list:\n>> "))
numbers = [int(input(f"Please enter number {a + 1} for your list:\n>> ")) for a in range(lenght_numbers_list)]
numbers.sort(reverse= True)
print(f"Your second-largest number is:{numbers[1]}")

#H. Ask the user for a list of integers and find the mean value of that list.
lenght_integers_list = int(input("Please enter the lenght of your numbers list:\n>> "))
integers = [int(input(f"Please enter number {_ + 1}:\n>> ")) for _ in range(lenght_integers_list)]
mean_value = sum(integers) / len(integers)
print(f"Your list mean value is:{mean_value}")

#I. Ask the user for a list of integers and find the third-smallest number in the list.
lenght_integers_list = int(input("Please enter the lenght of your numbers list:\n>> "))
integers = [int(input(f"Please enter number {_ + 1}:\n>> ")) for _ in range(lenght_integers_list)]
integers.sort()
print(f"Your third-smallest number is:{integers[2]}")

#J. Write a program that asks the user for three colors separated by spaces. The program should print all those colors using comma (you should use string 'join' method). For example:Your colors are red, blue, white.
list_colors = list(input("Enter 3 colors seperated by space:\n>> ").split())
modified_list_colors = ", ".join(list_colors)
print(f"Your colors list are:{modified_list_colors}")

#K. Write a program that asks the user for four capital cities separated by spaces. The program should print all those cities the following structure: There are many capital cities in the world. For example, Baku, Moscow and Kyiv. You should follow all instructions, and not make changes to the structure of final sentence.
list_capitals = list(input("Enter four capital cities separated by spaces:\n>> ").split())
print("There are many capital cities in the world. For example, {}, {} and {}.".format(*list_capitals[:3]))

#L. Take a list of strings as input and sort it in alphabetical order.
strings = input("Enter a list of strings separated by spaces: ").split()
strings.sort()
print(f"Your modified list:{strings}")

#M. Take a list of numeric values as input and sort it in descending order.
values = input("Enter a list of numeric values separated by spaces: ").split()
values_list = [float(x) for x in values]
values_list.sort(reverse=True)

#N. Remove duplicates from a list entered by the user while preserving the original order.
user_list = input("Enter a list separated by spaces: ").split()
modified_list = [set(user_list)]

#O. Write a program that accepts two lists and concatenates them into a single list. The first list is a list of fruits, the second is a list of vegetables.
fruits_list = input("Enter a list of fruits separated by spaces: ").split()
vegetables_list = input("Enter a list of vegetables separated by spaces: ").split()
combined_list = fruits_list + vegetables_list
print(combined_list)

#P. Write a program that prints 'True' if there is at least one item in a 'my_list' list.
my_list = [1, 2, 3, 4, 5]
result = bool(my_list)
print(result)

#- List Comprehension -
#Suppose you have the following lists:digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], letters = ['p', 'y', 't', 'h', 'o', 'n'], times = [1, 2, 3, 4, 5]
#
#A. Create a list containing raised to power two values of 'digits' list.
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
square_digits = [x**2 for x in digits]
print(square_digits)

#B. Create a list containing capitalized version of letter values of 'letters' list.
letters = ['p', 'y', 't', 'h', 'o', 'n']
capitalized_letters = [x.upper() for x in letters]
print(capitalized_letters)

#C. Create a list containing the 'Comprehension' string value the amount of 'times' list's length time.
times = [1, 2, 3, 4, 5]
new_list = ['Comprehension' for _ in range(len(times))]
print(new_list)

#D. Create a list containing 5 random integers between -5 and 5. find the second-smallest number in the list. The program should print 'True' if that number is negative, and 'False' otherwise.
import random



random_integers = [random.randint(-5, 5) for _ in range(5)]
random_integers.sort()
second_smallest = random_integers[1]
is_negative = second_smallest < 0
print(random_integers)
print(second_smallest)
print(is_negative)

#E. Create a list of 10 random numbers and find the maximum and minimum values.
numbers = [5, 89, 56, 54, 12, 53, 48, 91, 75, 29]
max_value = max(numbers)
min_value = min(numbers)
print("Random Numbers:", numbers)
print("Maximum Value:", max_value)
print("Minimum Value:", min_value)
#- Comments -
#A. One-line comment, if it's appropriate.
#B. Multi-line comment, if it's appropriate.
#
#- Chat GPT's Homework -
#A. Create a list of colors and write a function that duplicates each color in the list. For example, if the list contains "red," it should become ["red", "red"]. Print the modified list.
#colors = ["red", "blue", "green"]
#colors_list = colors.append(x) for x in colors
#print(colors_list)

colors = ["red", "blue", "green"]
duplicated_list = colors + [x for x in colors]
print(duplicated_list)

#B. How many methods do you know to create an empty list in Python? 
#[]
#list()

#C. Which list method is used to add an element to the end of a list?
#append()

#D. Write a Python code snippet to access the third element in a list named my_list. 
my_list = [1, 2, 3, 4, 5]
third_element = my_list[2]

#E. Which list method is used to remove the last element from a list? 
#pop()

#F. What list method is used to insert an element at a specific position?
#insert() 

#G. Write Python code to reverse a list called my_list in-place. 
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)

#H. How can you create a shallow copy of a list in Python? 
#.copy()
#[:]

#I. Which list method is used to count the number of occurrences of a specific element in a list? 
#count()
#J. Write a Python code snippet to concatenate two lists, list1 and list2. 
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
new_list = list_1 + list_2

#K. What list method can be used to sort a list in ascending order? 
#sort()

#L. Write Python code to remove the first occurrence of an element 'x' from a list. 
my_list = [1, 2, 3, 4, 3, 5]
my_list.remove(3)
print(my_list)

#M. Explain the difference between append() and extend() methods when adding elements to a list. 
#append() method adds a single element to the end of a list
#extend() method adds list's elements to the end of the list.

#N. Which list method can be used to remove all elements from a list? 
#clear()

#O. Write Python code to find the index of the first occurrence of an element 'x' in a list. 
your_list = [1, 2, 3, 4, 3, 5]
index_3 = your_list.index(3)
print(index_3)

#P. What list method can be used to remove and return an element from a specific index in a list?
#pop()

#Quiz.
#1. Which method is used to add an element to the end of a list in Python?
#    d) append()
#
#2. What is the purpose of the insert() method for lists in Python?
#    c) Add an element at a specific index in the list.
#
#3. Which list method is used to remove and return the last element of a list?
#    a) pop()  
#
#4. What does the extend() method do when used on a list in Python?
#    b) Adds a new list as elements to the existing list.
#
#5. Which list method is used to reverse the order of elements in a list in Python?
#    a) reverse()
#
#6. What does the sort() method do when used on a list in Python?
#    c) Sorts the list in ascending order.
#
#7. Which method is used to find the index of the first occurrence of an element in a list?
#    a) index()
#
#8. What is the purpose of the pop() method when used on a list in Python?
#    b) Removes and returns the last element of the list.
#
#9. How can you count the number of occurrences of a specific element in a list?
#    a) Use the count() method.
#
#10. How can you check if a list is empty in Python?
#    c) Use the len() function and check if it's equal to zero.
#
#11. Which method is used to copy the elements of one list to another in Python?
#    a) copy()
#
#12. How do you remove an element by index from a list in Python?
#    a) Use the remove() method with the index as an argument.
#
#13. What does the len() method do when applied to a list?
#    c) Returns the number of elements in the list
#
#14. Given the following list, what is the output of min(my_list)?
#    my_list = [0, 2, 4, 1, 5]
#    result = min(my_list)
#
#    a) 0
#
#15. Given the following list, what is the output of max(my_list)?
#    my_list = [0, 2, 4, 1, 5]
#
#    d) 5
#
#16. Which list method can be used to find the number of occurrences 
#of a specific element in a list?
#    a) count()
#
#17. What is the output of the following code snippet?
#    my_list = [1, 2, 3, 4, 5]
#    my_list.reverse()
#    print(my_list)
#
#    b) [5, 4, 3, 2, 1]
#
#18. What is the output of the following code snippet? 
#    my_list = [1, 2, 3] 
#    my_list.insert(1, 4) 
#    print(my_list)
#
#    b) [1, 4, 2, 3] 
#
#19. Which method is used to remove all elements from a list? 
#    a) clear() 
#
#20. What is the output of the following code snippet? 
#    my_list = [1, 2, 3, 4, 5] 
#    result = sum(my_list) 
#    print(result)
#
#    a) 15 
#
#21. What is the output of the following code snippet? 
#    my_list = [1, 2, 3, 4, 5] 
#    result = my_list.index(3) 
#    print(result)
#
#    d) 3
"""
shopping_cart = []
name = "Elmir"
age = 19
grade = "A"
a = name, age, grade
b = (print(x) for x in a)
print(b)