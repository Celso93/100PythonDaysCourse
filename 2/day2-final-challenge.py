print("Hello and Welcome to the tip calculator!")
bill = float(input('What was the total bill ? $'))
tip = float(input('How much tip would you like to give? 10, 12 or 15? '))/100
people = float(input('How many people to split the bill ? '))

total = bill + bill*tip
split_result = total/people
print(f'Each person should pay: ${round(split_result, 2)}')
