"""
BMI Calculator with Interpretations
Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.
If the bmi is under 18.5 (not including), print out "underweight"
If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"
If the bmi is 25 (including) or over, print out "overweight"
"""

print("Welcome to the BMI calculator")
height = float(input("Type your height(m): "))
weight = float(input("Type your weight(kg): "))

bmi = weight/(height**2)

if bmi >= 25:
    print(f"Your BMI is {bmi}: so your are overweight")
elif bmi >= 18.5 and bmi < 25 :
    print(f"Your BMI is {bmi}: so your are normal weight")
else:
    print(f"Your BMI is {bmi}: so your are underweight")