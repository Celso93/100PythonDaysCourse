# exercise: Check Odd (impar) or even (par)

number = float(input("Type your number: "))
number %= 2

if number == 0:
    print(f"the remaining is:{number} so this a even")
else:
    print(f"the remaining is:{number} so this a odd")