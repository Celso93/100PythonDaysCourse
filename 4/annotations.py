import random
import example_of_module

random_number = random.randint(1, 10)
print(random_number)

'''
Modules in python ?
You can create a new module simply by creating a new .py file, 
and then you can import variables or functions from that file just by using the import keyword.
'''
print(example_of_module.teste_module)

# float number
rand_num_0_to_1 = random.random()
print(rand_num_0_to_1)
print(rand_num_0_to_1 * 5)
print(random.uniform(1,10))

'''
Exercise
Heads or Tails
Create a coin flip program using what you have learnt about randomisation in Python. 
It should randomly print "Heads" or "Tails" everytime it is run.
'''

coin = random.sample(["Heads", "Tails"], k=1)
print(coin)
