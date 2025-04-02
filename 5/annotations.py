'''
Loops allow us to tell the computer to repeat actions without having to write repeated code. If we wanted the computer to print out 1 through to 100, it would very painful to type a print statement for every number, or even just typing out all the numbers 1 through to 100. Loops allow us to create a rule and the computer can follow it to do a repeated action.

Syntax
for <variable name of each item> in <a List>:
    <do something>
    <do something else> 
PAUSE 1 - Be a Computer
Predict what will be printed from the code below:

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " pie")

Sum
Python has lots of built-in functions to help us work with numbers. One of them helps us calculate the sum (the total). e.g.

student_scores = [180, 124, 165, 173, 189, 169, 146]
total_score = sum(student_scores) 
But how does sum() work behind the scenes? The code is written by the people who developed Python and it might look something like this:

student_scores = [180, 124, 165]

sum = 0
for score in student_scores:
    sum += score
    
print(sum)
'''

