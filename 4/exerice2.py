
import random

#Figure out how to pick a random name from the list of friends.
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
random_number = random.randint(0, 4)
print(friends[random_number])

# more simple
print(random.choice(friends))
