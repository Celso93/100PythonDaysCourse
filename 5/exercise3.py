'''
FizzBuzz
You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
Your program should print each number from 1 to 100 in turn and include number 100.
But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

e.g. it might start off like this:

1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
...etc
'''

numbers = []

for number in range(0, 100):
    if number%3 == 0 and number%5 == 0:
        numbers.append("FizzBuzz")
    elif number%5 == 0:
        numbers.append("Buzz")
    elif number%3 == 0:
        numbers.append("Fizz")
    numbers += number
    
print(numbers)
