"""
- Dictionaries -
A. Create a dictionary with you personal data (firstname, lastname, age, gender).
B. Create a dictionary with stock data of fruits (fruit name, amount in stock).
C. Change any value of the dictionary from Task B.
D. Create a dictionary about five students and their math grades.
E. Add some points to any student from Task D's dictionary.
F. Create a dictionary about your favorite car model. Describe it as much 
as you can (brand, manufacturing contry, tires, color, year).
G. Create a dictionary with all continents of the world with minimum 3 
countries (if possible) as its value.
H. Create a dictionary with minimum 5 key-value pairs. Use any english word as keys, 
and definition of those words as values. Print dictionary and its length.
I. Create a dictionary with minimum 5 key-value pairs. Use any english word as keys, 
and translation to russian language of those words as values.
J. Fill in the blank:
As of Python version _._, dictionaries are ordered. In Python _._ and earlier, 
dictionaries are unordered.
K. Describe dictionaries' main 3 characteristics
L. Fill in the blank:
Only _______ objects or data types can be represented as keys in dictionaries.
M. Print all keys of dictionary from Task D.
N. Print all values of dictionary from Task D.
O. Print all keys and values together of dictionary from Task D.
P. Suppose you have the following code snippet:

car = {
    "model": "Camaro",
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "brand": "Chevrolet",
    "color": "red",
}
print(car)

What will be the output of the program and why?
Q. Change 'color' of 'car' dictionary to 'blue'.
R. Add any new key-value pair to 'car' dictionary.
S. Use the whole dictionary from Task A in a string formatted with:
    1. f-strings
    2. format
    3. %s
T. Create an empty dictionary. Print its length.
U. You have the following dictionary:
grades = {
    'Alice': 85,
    'Bob': 90,
    'Charlie': 78,
    'David': 92,
    'Emily': 88
}

Ask user for a student name to add 7 points to the grade of that student.
V. You have the following dictionary:
word_definitions = {
    'apple': 'a round fruit with red or green skin and crisp flesh',
    'computer': 'an electronic device for processing and storing data',
    'book': 'a written or printed work consisting of pages',
    'ocean': 'a large body of saltwater that covers most of the Earth\'s surface',
    'mountain': 'a large natural elevation of the Earth\'s surface'
}

Ask user for an item name to to print the length of the definition of that item.

- ChatGPT's homework (Dictionaries) -
A. Create a dictionary named student_scores with the following key-value pairs:

    "Alice": 85
    "Bob": 92
    "Eve": 78
    "Charlie": 95

Print out the dictionary student_scores.
B. Add a new student "David" with a score of 88 to the dictionary.
C. Update Eve's score to 82.
D. Remove Bob from the dictionary.
E. Create a Python program that asks the user to enter a key, and then prints 
the corresponding value from the provided dictionary. If the key does not exist, 
it should print a message saying "Key not found.":
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
F. Create a Python program that asks the user to enter a key and a value, and then 
adds this key-value pair to the provided dictionary:
1. Ask the user to enter a key and a value.
2. Add the entered key-value pair to the provided dictionary my_dict.
3. Print the updated dictionary.

- I/O -
A. Write a program that gets the sides of a rectangle from the user, and
calculates its perimeter.
B. Write a program that gets the sides of a rectangle from the user, and
calculates its area.
C. Write a program that gets the sides of a square from the user, and
calculates its perimeter.
D. Write a program that gets the sides of a square from the user, and
calculates its area.
E. Write a program that gets the radius of a circle from the user, and
calculates its area.
F. Write a program that gets the diameter of a circle from the user, and
calculates its length.

- Comments -
A. One-line comment in any random three places of your code, if it's appropriate.
B. Multi-line comment anywhere in your code, if it's appropriate.

Quiz.
1. What is a dictionary in Python?
    a) A collection of elements with index positions
    b) A collection of key-value pairs
    c) A collection of unique elements
    d) A collection of elements in a specific order

2. How do you create an empty dictionary in Python?
    a) my_dict = {}
    b) my_dict = dict()
    c) my_dict = new dict()
    d) my_dict = dict{}

3. How do you access a value in a dictionary using its key?
    a) my_dict.get(key)
    b) my_dict[key]
    c) my_dict.value(key)
    d) my_dict.access(key)
    
4. Can a dictionary have duplicate keys?
    a) Yes
    b) No
    
5. How do you add a new key-value pair to an existing dictionary?
    a) my_dict.add(key, value)
    b) my_dict[key] = value
    c) my_dict.insert(key, value)
    d) my_dict.append(key, value)
    
6. How do you remove a key-value pair from a dictionary?
    a) my_dict.remove(key)
    b) my_dict.delete(key)
    c) del my_dict[key]
    d) my_dict.pop(key)
    
7. Which method returns a list of all the keys in a dictionary?
    a) my_dict.keys()
    b) my_dict.get_keys()
    c) my_dict.key_list()
    d) my_dict.all_keys()

8. How do you check if a key is in a dictionary?
    a) key in my_dict
    b) my_dict.has_key(key)
    c) my_dict.contains(key)
    d) my_dict.is_key(key)

9. What happens if you try to access a key in a dictionary that doesn't exist?
    a) It raises a KeyError
    b) It returns None
    c) It raises a ValueError
    d) It raises an IndexError

10. Which dictionary method is used to retrieve the value associated with a key, 
and if the key does not exist, return a default value instead of raising an error?
    a) get(key, default)
    b) retrieve(key, default)
    c) value(key, default)
    d) find(key, default)

11. Which dictionary method is used to remove all key-value pairs from the dictionary?
    a) clear()
    b) delete_all()
    c) remove_all()
    d) erase()

12. Which dictionary method returns a new dictionary with keys from the given sequence and 
values set to a specified value?
    a) fromkeys(seq, value)
    b) setkeys(seq, value)
    c) assign_keys(seq, value)
    d) create_keys(seq, value)

13. Which dictionary method returns a list of tuples, each tuple containing a key-value pair 
from the dictionary?
    a) items()
    b) pairs()
    c) tuples()
    d) entries()

14. Which dictionary method returns a list of all the values in the dictionary?
    a) values()
    b) all_values()
    c) retrieve_values()
    d) get_values()

15. Which dictionary method returns and removes an element with a specified key?
    a) pop(key)
    b) remove(key)
    c) delete(key)
    d) extract(key)
    
16. Which dictionary method returns a shallow copy of the dictionary?
    a) copy()
    b) clone()
    c) duplicate()
    d) replicate()

17. Which dictionary method is used to update the dictionary with key-value pairs 
from another dictionary or from an iterable of key-value pairs?
    a) update(iterable)
    b) merge(iterable)
    c) add(iterable)
    d) append(iterable)

18. Which dictionary method returns the value for a specified key and removes the 
key-value pair from the dictionary?
    a) popitem()
    b) removeitem()
    c) deleteitem()
    d) extractitem()
    
19. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(my_dict.get('b'))

    a) 1
    b) 2
    c) 'b'
    d) None
        
20. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_dict['d'] = 4
    print(my_dict)
    
    a) {'a': 1, 'b': 2, 'c': 3}
    b) {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    c) {'d': 4}
    d) {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
21. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_dict.pop('b')
    print(my_dict)

    a) {'a': 1, 'c': 3}
    b) {'a': 1, 'b': 2, 'c': 3}
    c) 'b'
    d) {'b': None}

22. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    print(list(my_dict.items()))

    a) [('a', 1), ('b', 2), ('c', 3)]
    b) {'a': 1, 'b': 2, 'c': 3}
    c) ('a', 1), ('b', 2), ('c', 3)
    d) ['a', 1, 'b', 2, 'c', 3]
    
23. What will be the output of this code:
    my_dict = {'a': 1, 'b': 2, 'c': 3}
    my_dict.update({'b': 5, 'd': 4})
    print(my_dict)

    a) {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    b) {'a': 1, 'b': 5, 'c': 3, 'd': 4}
    c) {'a': 1, 'b': 2, 'c': 3}
    d) {'a': 1, 'b': 5, 'c': 3}

24. What is the main difference between the pop() and popitem() methods in Python dictionaries?
    a) pop() allows you to remove a specific key-value pair by providing the key, while popitem() 
    removes and returns an arbitrary key-value pair.
    b) pop() removes the last key-value pair added to the dictionary, while popitem() removes 
    the first key-value pair.
    c) pop() removes a key-value pair based on its index, while popitem() removes a key-value 
    pair based on its key.
    d) pop() removes and returns a random key-value pair from the dictionary, while popitem() 
    removes and returns the first key-value pair.
"""