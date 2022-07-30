import random

# generate random_module number in range (x to y) inclusive
print(random.randint(1, 1000))

# random between 0 and 1
print(random.random())

# shuffle items in list
fruits = ['apple', 'banana', 'orange']
random.shuffle(fruits)
print(fruits)

# random from list
print(random.choice(fruits))
print(random.choices(fruits, k=2))  # k - number of elements
print(random.sample(fruits, k=2))  # unique elements from list (no repeat)
