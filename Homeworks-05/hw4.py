#
#- Strings -
#A. Create a variable called 'long_sentence'. Make it equal a sentence minimum. Print 'long_sentence's length.
long_sentence = "sentence minimum"
print(len(long_sentence))

#B. Replace Print function's 'end' parameter from default '\n' to '\t'. Write 2 Print functions with it.
fruit = "apple"
fruit2 = "melon"
print(fruit, end="\t")
print(fruit2)

#C. Change Print function's 'end' parameter, so that it links values with stars. Example: Today*is*a*good*day!
print("Today", end="*")
print("is", end="*")
print("a", end="*",)
print("good", end="*",)
print("day!")

#D. Write 3 different Print functions with according string ("He", "is", "cool.") in such way so you can see this on your console (you can use any method): He is cool.
print("He", end=" ")
print("is", end=" ")
print("cool.")

#E. The same task as previous (D), but now make it look like: He#is#cool.
print("He", end="#")
print("is", end="#")
print("cool.")

#F. Create a variable named 'color'. Give it a string 'Python' value.
color = "Python"

#G. Create a variable named 'item'. Give it a string 'Developer' value.
item = "Developer"

#H. Use all methods you know about string-formattings and Print function to concatenate these two variables, so you can see 'Python Developer' on your console (terminal).
#Metod 1
print(f"{color} {item}")
#Metod 2
print("{} {}".format(color, item))
#metod 3
print("%s %s" % (color, item))

#I. Replace Print function's 'end' parameter from default value to '...'. Write 3 Print functions with it.
print("Bu" , end="...")
print("çox" , end="...")
print("yorucudur")
#J. Suppose you have the following variable: word = "Hello. I am Taylor."

#j
#Using slicing method:
#1. Create a variable called 'prefix'. Make it equal to 'Hello.' part of 'word' variable.
#2. Create a variable called 'middle_part'. Make it equal to ' I am ' part of 'word' variable.
#3. Create a variable called 'name'. Make it equal to 'Taylor.' part of 'word' variable.
#
#Create a variable named 'recreated_word' or 'result' and use all previous variables 
#(prefix, middle_part, name) to recreate the 'word' phrase.
word =  "Hello. I am Taylor"
        #012345678901234567
prefix = word[:6]
middle_part = word[6:12]
name = word[12:]
result = prefix + middle_part + name
print(result)
#K. Suppose you have the following value: "abababababa"
#
#Using slicing method, get all 'a' characters from the value and assign it to a variable, then print that variable.
word = "abababababa"
new_word = word[0::2]
print(new_word)

#L. Create a formula that finds the last index of a string.
word = "Elmir"
print(len(word) - 1)

#M. What is the difference between 1 and "1"? Are they equal values, why?
a = "1"
b = 1
print(type(a), type(b))

#N. Using all your Python knowledge, find the amount of words the following sentence:"The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
sentence = "The mission of the Python Software Foundation is to promote, protect, and advance the Python programming language, and to support and facilitate the growth of a diverse and international community of Python programmers."
print(sentence.count(" ") + 1)

#- String Methods -
#A. Use all these string methods and test it in your code:

#1. title
word = "elmir"
print(word.title())
#2. capitalize
print(word.capitalize())
#3. count
print(word.count("e"))
#4. endswith
print(word.endswith("*"))
#5. find
print(word.find("l"))
#6. index
print(word.index("m"))
#7. isalpha
print(word.isalpha())
#8. isdigit
print(word.isdigit())
#9. islower
print(word.islower())
#10. isupper
print(word.isupper())
#11. lower
word = "Elmir"
print(word.lower())
#12. upper
print(word.upper())
#13. replace
print(word.replace("E", "A"))
#14. split
word = "Elmir*Seymur"
print(word.split("*"))
#15. strip
word = "   Elmir"
print(word.strip())
#16. startswith
word = "Elmir"
print(word.startswith("*"))
#17. join
word = ("Elmir", "Seymur")
print("*".join(word))

#B. Combine several string methods at once.
word = "   elmir, how are you today?  "
new_word = word.strip().replace("today", "yesterday").capitalize()
print(new_word)

#C. Create any string-valued variable. First, call the 'lower' method on it, then call 'islower' method. What value will it always give you and why?
word = "Elmir"
print(word.islower())
print(word.lower().islower())

#D. Suppose you have the following variable: my_value = "Obviously, today is a hot day."Replace all 'o' characters with 0 (zeros). 
my_value = "Obviously, today is a hot day."
new_value = my_value.replace("o", "0")
print(new_value)

#E. Count how many times the word 'likes' occured in the following string: "Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile."
print("Sammy likes to swim in the ocean, likes to spin up servers, and likes to smile.".count("likes"))

#- String Formattings -
#A. Create a variable 'name' and assign your name to it. Create a variable 'age' and assign your age to it. Using the f-string method, create a formatted string that displays your name  and age in the following format: "My name is [name] and I am [age] years old."
name = "Elmir"
age = "19"
sentence = "My name is {} and I am {} years old".format(name, age)
print(sentence)

#B. Create a variable item and assign a string representing an item name. Create a variable quantity and assign an integer representing the quantity of the item. Create a formatted string using the old-style % formatting that displays the item  name and quantity in the following format: "I want to buy %d units of %s."
item = "pen"
quantity = 10
print( "I want to buy %d units of %s." % (quantity, item))

#C. Make your best and create a hard task by your own using string formattings.
#
#- Chat GPT's Homework -
#A. Use the len() function to find the length of the following strings:
#1. "programming"
print(len("programming"))
#2. "python is fun"
print(len("python is fun"))
#3. "12345"
print(len("12345"))

#B. Convert the following string to uppercase string:
#"hello world"
print("hello world".upper())

#C. Check if the string "python" is present in the following sentence:
#"I enjoy programming in Python."
print("python" in "I enjoy programming in Python.")

#D. Given the string "programming", access the following elements using positive and negative indexing:
#1. The first character
word = "programing"
print(word[0])
#2. The last character
print(word[-1])
#3. The third character
print(word[3])
#4. The second-to-last character
print(word[-2])

#E. Using string slicing, extract the word "is" from the string: "Python is a versatile programming language."
sentence = "Python is a versatile programming language."
word = sentence[7:9]
print(word)

#F. Retrieve the substring "quick brown" from the following sentence:
#"The quick brown fox jumps over the lazy dog."
sentence = "The quick brown fox jumps over the lazy dog."
print(sentence[4:15])

#G. Reverse the following string using slicing:
#"redivider"
word = "redivider"
print(word[::-1])

#H. Write a program that capitalizes the first letter of each word in the following sentence:
#"welcome to the world of programming"
sentence = "welcome to the world of programming"
print(sentence.title())

#- Interview Questions -
#A. Reverse any string using slicing method.
string = "elmir"
print(string[::-1])

#B. Print the whole string using slicing method, not knowing the length of a string.
#
#- Comments -
#A. One-line comment in any random three places of your code, if it's appropriate.
#B. Multi-line comment anywhere in your code, if it's appropriate.
#
#Quiz:
#A. What does len('Hello ') return?
#    a) 4
#    b) 5
#               c) 6
#    d) 'Hello'
#    e) "Hello"
#
#B. What is the output of the following code snippet:
#
#    sphere = "Web Development" * 2 + "" * 6
#    length = len(sphere)
#    print(length)
#
#    a) 15
#    b) 20
#    c) 25
#               d) 30
#
#C. Which of the operator can be used in Strings?
#    a) +
#    b) *
#                       c) Both of the above
#    d) None of the above
#
#D. What is the output of the following code snippet:
#
#    comment = "I like your blue pants"
#    pattern = comment[19:4:-3]
#    print(pattern, len(pattern))
#
#               a) "n lry", 5
#    b) "n lry", 4
#    c) "n ly", 4
#    d) "p ly", 4
#    e) "p l ", 4
#
#E. Is the following variable named correctly, why?
#
#    myVariable = "Python is best!"
#
#    a) yes, follows the rules of naming a variable, pythonic code
#                       b) no, doesn't follow the rules of naming a variable, non-pythonic code
#    c) it depends on the code editor you type
#    d) it's not a code written in Python
#"""
word = "Elmir"
print(word[-1:200:-1])