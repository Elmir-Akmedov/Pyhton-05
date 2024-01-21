"""
#Note. All tasks should be written as in the following example (you can
#use variable naming method or adding a comment after the expression):
## A
#expression = True and False or True
#step_one = (True and False) or (True)
#step_two = (False) or (True)
#step_three = True
#print(step_three == expression)
#
#At the end, your program should only print 'True's, so that will mean
#you have accomplished and simplified all expressions correctly.
#
#- Booleans -
#Simplify these expressions:
#A. True or False and True
expression = True or False and True
step_one = True or (False and True)
step_two = (True) or (False)
step_three = True
print(step_three == expression)

#B. False and False or False
expression = False and False or False
step_one = (False and False) or False
step_two = False or False
step_three = False
print(step_three == expression)

#C. (True or False) and True
expression = (True or False) and True
step_one = True and True
step_two = True
print(step_two == expression)

#D. True or (True or False and True) and True
expression = True or (True or False and True) and True
step_one = True or (True or (False and True)) and True
step_three = True or (True or False) and True
step_four = True or True and True
step_five = True or True
step_six = True
print(step_six == expression)

#E. False or False and False and not False
expression = False or False and False and not False
step_one = False or (False and False and True)
step_two = False or (False and True)
step_three = False or False
step_four = False
print(step_four == expression)

#F. (True or True or False) and True
expression = (True or True or False) and True
step_one = (True or False) and True
step_two = True and True
step_three = True
print(step_three == expression)

#G. False or (True and False)
expression = False or (True and False)
step_one = False or (False)
step_two = False
print(step_two == expression)

#H. False and False and False and False and False or True and False
expression = False and False and False and False and False or True and False
step_one = False and False and False and False or True and False
step_two = False and False and False or True and False
step_three = False and False or True and False
step_four = False or True and False
step_five = True and False
step_six = False
print(step_six == expression)

#I. True or False or True
expression = True or False or True
step_one = True or True
step_two = True
print(step_two == expression)

#J.True or False or True
expression = True or False or True
step_one = True or True
step_two = True
print(step_two == expression)

#K. not True or not False
expression = not True or not False
step_one = False or True
step_two = True
print(step_two == expression)

#L. False and not False or not False
expression = False and not False or not False
step_one = False and True or True
step_two = False or True
step_three = True
print(step_three == expression)

#M. True or not False and True or not not True
expression = True or not False and True or not not True
step_one = True or True and True or True
step_two = True or True and True
step_three = True or True
step_four = True
print(step_four == expression)

#N. not not not False
expression = not not not False
step_one = True
print(step_one == expression)

#O. not N (previous task N's value)
expression = not not not not False
step_one = not not False
step_two = False
print(step_two == expression)

#P. True or False and not True or (not True and False) and not True or False
expression = True or False and not True or (not True and False) and not True or False
step_one = True or False and False or (False and False) and False or False
step_two = True or False and False or False and False or False
step_three = True or ((False and False) or ((False and False) or False))
step_four = True or (False or (False or False))
step_five = True or (False or False)
step_six = True or False
step_seven = True
print(step_seven == expression)

#Q. True or not False or not True or True
expression = True or not False or not True or True
step_one = True or True or False or True
step_two = True or False or True
step_three = True or True
step_four = True
print(step_four == expression)

#R. False and (not True or False or (False or not True and True or False)) and True
expression = False and (not True or False or (False or not True and True or False)) and True
step_one = False and (False or False or (False or False and True or False)) and True
step_two = False and (False or False or (False or ((False and True) or False))) and True
step_three = False and (False or False or (False or (False or False))) and True
step_four = False and (False or False or (False or False)) and True
step_five = False and (False or False or False) and True
step_six = False and (False or False) and True
step_seven = False and False and True
step_eight = False and True
step_nine = False
print(step_nine == expression)

#S. False and not not not True and (False or True or not False) and True or False
expression = False and not not not True and (False or True or not False) and True or False
step_one = False and False and (False or True or True) and True or False
step_two = False and False and (True or True) and True or False
step_three = False and False and True and True or False
step_four = (False and True and True) or False
step_five = (False and True) or False
step_six = False or False
step_seven = False
print(step_seven == expression)

#T. not (True or False) or not False or (True and False or False)
expression =  not (True or False) or not False or (True and False or False)
step_one =  False or not False or (True and False or False)
step_two =  False or True or (True and False or False)
step_three = False or True or (False or False)
step_four = False or True or False
step_five = True or False
step_six = True
print(step_six == expression)

#U. (True or not not False) and (True or (True or (False)))
expression = (True or not not False) and (True or (True or (False)))
step_one = (True or not not False) and (True or True)
step_two = (True or not not False) and True
step_three = (True or False) and True
step_five = True and True
step_six = True
print(step_six == expression)

#V. False and False or (not False and (not False))
expression = False and False or (not False and (not False))
step_one = False and False or (True and True)
step_two = False and False or True
step_three = False or True
step_four = True
print(step_four == expression)

#W. (not True or not False) and (not True or (not False))
expression = (not True or not False) and (not True or (not False))
step_one = (False or True) and (False or True)
step_two = True and (False or True)
step_three = True and True
step_four = True
print(step_four == expression)

#X. False or False and not True or not False and (not True and False)
expression = False or False and not True or not False and (not True and False)
step_one = False or False and False or True and (False and False)
step_two = False or False and False or True and False
step_three = False or ((False and False) or (True and False))
step_five = False or (False or (True and False))
step_six = False or (False or False)
step_seven = False or False
step_eight = False
print(step_eight == expression)

#Y. True and True and True and True and not True and True and True or False
expression = True and True and True and True and not True and True and True or False
step_one = (True and True and True and True and False and True and True) or False
step_two = (True and True and True and False and True and True) or False
step_three = (True and True and False and True and True) or False
step_four = (True and False and True and True) or False
step_five = (False and True and True) or False
step_six = (False and True) or False
step_seven = False or False
step_eight = False
print(step_eight == expression)

#Z. False and False and (True or not False and (True or False and True)) or not True and False and (not False or not True)
expression = False and False and (True or True and (True or False and True)) or False and False and (True or False)
step_one =  False and False and (True or True and (True or False)) or False and False and (True or False)
step_two =  False and False and (True or True and True) or False and False and (True or False)
step_three =  False and False and (True or True and True) or False and False and True
step_four =  False and False and (True or True) or False and False and True
step_five =  False and False and True or False and False and True
step_six =  (False and True) or (False and False and True)
step_seven = False or (False and False and True)
step_eight = False or (False and True)
step_nine = False or False
step_nine = False
print(step_nine == expression)
"""
colors = ["red", "blue", "green"]
colors_list = colors.copy()
colors_list = [colors.append(x) for x in colors_list]
print(colors_list)