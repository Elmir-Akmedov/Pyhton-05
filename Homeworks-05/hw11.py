#- Tuples -
#A. Create a tuple containing minimum seven different colors.
colors = ("black", "green", "red", "white", "purple", "blue", "grey")

#B. Create a tuple containing minimum five different countries.
countries = ("USA", "England", "China", "Russia", "Germany")

#C. Create a tuple containing three string values and two integer values.
mix_tuple = ("USA", "England", "China", 89,25)

#D. Create a tuple containing all continents of the world.
continents = ("Eurasian", "Asia", "Africa", "Australia", "N.America", "S.America", "Antarctica")

#E. Create a tuple containing minimum four car brands.
car_brands = ("Dodge", "Ford_Mustang", "Tayota_Supra", "Ford_Raptor", "McLaren")

#F. Create a tuple containing four different data types of Python.
data_types = ("String", "Boolean", "NoneType", "Ineteger", "List", "Dictionary", "Tuple")

#G. Create a tuple containing only negative even numbers from -2 to -12.
negative_numbers = tuple(range(-2, -13, -2))
new_numbers = tuple(range(-12, -1, 2))
print(new_numbers)
print(negative_numbers)

#H. Create a tuple containing only positive even numbers from 0 to 12.
positive_numbers = tuple(range(12, 0, -2))
new_numbers = tuple(range(0, 12, 2))

#I. Combine tuples from Task G and H.
combined_numbers = tuple(sorted(negative_numbers + positive_numbers))

#J. Create a tuple containing minimum six students' names. Print the first student's name.
students = ("Elmir", "Seymur", "Ayxan", "Jack", "Tom", "Baki", "Jessica")
print(students[0])

#K. Create a tuple containing three different integers. Print the integer at position two.
integers = (1, 2, 3)
print(integers[1])

#L. Print the last element of Task D's tuple.
print(continents[-1])

#M. Print the last two elements of Task A's tuple. You can use slicing method only once. Separately printing those elements will not be accepted.
print(*colors[-2:], sep="")

#N. Given the following tuple: double_me = (0, 5, 10). Create a new tuple containing the double value of that tuple.
double_me = (0, 5, 10)
doubled_tuple = double_me * 2

#O. Create any nested tuple. Print any value from the inner tuple and the whole inner tuple.
nested_tuple = ((1, 2, 3), ('a', 'b',), (True, False,))
print(nested_tuple[0][2])
print(nested_tuple[1])

#P. Change the value of the color at position six of the tuple from Task A.
colors_list = list(colors)
colors_list[6] = "orange"
colors = tuple(colors_list)

#Q. From Task B's tuple print all countries except the first two.
print(countries[2:])

#R. Create two new tuples containing the double value of the tuple from Task F 
#using 2 different mathematical operations.
data_types_2 = data_types * 2
data_types_3 = data_types + data_types

#S. Create an empty tuple.
empty_tuple = tuple()

#T. Create a tuple with only the one 'Python' string value. Print its type.
just_tuple = ('Python',)

#U. Count how many times the word 'hacking' appears in this tuple:
black_hat = ('hacking', 'hiding', 'hiking', 'hacking', 'viking', 'horsing', 'black', 'hat', 'hacking')
hacking_count = black_hat.count('hacking')
print(hacking_count)

#V. Count how many 'True's are in this tuple:
booleans = (True, True, False, True, False, False, True)
true_count = booleans.count(True)
print(true_count)

#W. Find the position of the first 'a' character in the following tuple:
randomized_alphabet = ('b', 'w', 'v', 't', 'n', 'c', 'd', 'a', 'f', 'a')
position_a = randomized_alphabet.index('a')

#X. When should you consider using constant variables with tuples in your Python code? 
#Provide an example scenario.
CONFIG_SETTINGS = ('DEBUG_MODE', 'LOG_LEVEL', 'MAX_CONNECTIONS')
print(CONFIG_SETTINGS[2])

#Bonus:

#A. Print the whole tuple from previous tasks using the slicing method.
print(colors[:])

#B. Print the length of any tuple from previous tasks.
print(len(colors))

#- Sets -
#You have the following set:
ages = {12, 14, 16, 18, 20, 22, 24, 26}

#A. Write a Python program to remove an item from the 'ages' set if
#it is present in the set.
ages.remove(18)

#B. Add 28 to 'ages' set.
ages.add(28)

#C. Copy this set. Check if this copied set is a subset of the original set.
ages_copy = ages.copy()
is_subset = ages_copy.issubset(ages)

#D. Check if the following set is a subset of the 'ages' set:
suspected_subset = {12, 14}
is_subset = suspected_subset.issubset(ages)

#E. Remove 12 and 14 from the 'ages' set.
ages.difference_update({12, 14}) ###

#F. You have the following tuple and set:
names = ('Murad', 'Aysel', 'Gunel')
students = {'Bob', 'John'}
students.update(names)
#Extend the 'students' set with the 'names'.

#G. Find the difference between the following sets:
fruits = {"apple", "banana", "cherry"}
items = {"google", "microsoft", "apple"}
difference_set = fruits.difference(items)

#H. Print the length of the 'ages' set. Then add 12 to the 'ages' set. Print the
#length again.
print(len(ages))
ages.add(12)
print(len(ages))

#I. Clear the 'ages' set. Print it and its length.
ages.clear()
print(ages, len(ages))

#- Interview Questions -

#A. Reverse a tuple with slicing method.
anything = (2, 5, 9)
print(anything[::-1])

#B. What's the main difference between Tuples and Lists in Python?
#mutability

#C. What's the best practice to use Sets, and not Lists or Tuples?
#sets opretaions

#D. What's the difference between Set's 'remove' and 'discard' method?
#Remove an element from a set; it must be a member.If the element is not a member, raise a KeyError.

#E. You have the following list of the students of 7th grade class:
names = ["Murad", "Mike", "Murad", "Elcin", "Vuqar", "Murad", "Nargiz"]

#How can you remove all duplicate names from this list?
modified_names = set(names)
names = list(modified_names)
print(names)

#F. When might you choose to use a set instead of a list or tuple in Python? 
#Provide an example scenario.
new_sets = {"elmir", "seymur"}
new_sets.add("Ayxan")
print(new_sets)

#- Comments -

#A. One-line comment in any random three places of your code, if it's appropriate.
#B. Multi-line comment anywhere in your code, if it's appropriate.
#
#- Chat GPT's Homework -

#A. Create a Python tuple named student_info that contains the following information about a student:
#1. Student's name
#2. Student's age
#3. Student's grade (as a string, e.g., "A" or "B")

name = "Elmir"
age = 19
grade = "A"
student_info = (f"{name}, {age} ,{grade}")
#B. Create an empty list called shopping_cart. Then, perform the following operations:
#1. Add three items to the shopping cart.
#2. Remove one item from the shopping cart.
#3. Modify one of the items in the shopping cart.
shopping_cart = []
for x in [name, age, grade]:
    shopping_cart.append(x)
print(shopping_cart)
shopping_cart.remove(name)
shopping_cart[1] = 30
print(shopping_cart)

#C. Create a tuple named coordinates containing latitude and longitude values. 
#Then, use tuple unpacking (*) to assign these values to separate variables called latitude and longitude. 
#Print the values of latitude and longitude.
coordinates = (12.5, 35.2)
latitude, longitude = [*coordinates]
print(latitude)
print(longitude)

#D. Explain in your own words the main differences between tuples and lists in Python.
#Provide examples of situations where you would use one over the other.

#Quiz.
#1. What is a tuple in Python?
#    d) An unordered collection of elements that is immutable.
#
#2. How do you create an empty tuple in Python?
#    e) empty_tuple = tuple()
#    f) empty_tuple = tuple(list())
#
#3. Question 3: Which of the following statements is true about sets in Python?
#    c) Sets are indexed using integers.
#    
#4. What is the primary purpose of using sets in Python?
#    b) To ensure elements are unique and eliminate duplicates.
#    
#5. Which of the following is true about the elements of a set in Python?
#    d) Elements of a set can be of different data types.
#    
#6. What is the result of the following code?
#    my_set = {1, 2, 3}
#    my_set.add(4)
#    my_set.remove(2)
#
#    b) {1, 3, 4}   
#
#7. Which of the following set operations returns the elements that are common to two sets?
#    a) union()
#
#8. Can a tuple contain elements of different data types?
#    a) Yes    
#    
#9. What is the key difference between a tuple and a list in Python?
#    c) Lists are unordered and mutable, while tuples are ordered and immutable.
#    
#10. Which of the following is a valid way to create a set in Python?
#    a) my_set = {1, 2, 3}
#
#11. Which of the following statements is true about tuples in Python?
#    c) Tuples can contain duplicate elements.
#
#12. What is the advantage of using tuples over lists in Python?
#    c) Tuples are faster for accessing elements.
#
#13. Which of the following list comprehensions creates a tuple of squares of numbers from 1 to 5?
# None
#
#14. What is the primary advantage of using sets when dealing with collections of data?
#    c) Sets ensure elements are unique.
# 
#15. In Python, what would be the result of applying the union() operation on two sets that 
#have some overlapping elements?
#    b) The operation will return all elements from both sets with duplicates removed.  
#    
#16. How can you remove an item from a list without knowing its index?
#    a) Using the remove() method.   
#
#17. Which of the following statements is true about list comprehensions?
#    d) List comprehensions always create a new list.
#
#18. What is the difference between the discard() and remove() methods for sets in Python?
#    a) discard() removes an element if it exists; remove() raises an error if the element is not found.
#    
#19. In Python, can a list contain elements of different data types?
#    a) Yes
#    
#20. In Python, what is a constant variable?
#    c) A variable whose value should not change after it's initially assigned.
#
#21. Which data structure in Python is commonly used to define constant variables?
#    b) Tuples
#
#22. How do you define a constant variable using a tuple in Python?
#    a) constant_var = (value)
#
#23. When defining constant variables using tuples, what is the recommended naming convention?.
#    b) Use uppercase letters with underscores (e.g., MY_CONSTANT_VAR).
#
#24. Which of the following operations is valid for a constant variable defined using a tuple?
#    b) Accessing its elements.
#
#25. Why might you choose to use a constant variable defined with a tuple instead of a regular variable?
#    c) To ensure that the variable's value remains constant.
#
#26. Which of the following code examples correctly defines a constant variable using a tuple?
#    a) const_var = (3.14, 'hello', True)
#
#27. What is the advantage of using constant variables with tuples over hardcoding values directly into your code?
#    c) It saves memory.
#
#28. In Python, can you reassign a value to a constant variable defined using a tuple?
#    a) Yes,because
#
#29. What does the asterisk (*) operator do when used with a variable in Python?
#    c) Allows the variable to hold multiple values, like a list or tuple.
#
#30. In Python, what does the from module_name import * statement do when importing a module?
#    a) It imports all functions, classes, and variables from the module.
#
#31. When might it be appropriate to use the asterisk () in a module import statement?
#    b) When you want to import all contents of the module for convenience.
#
