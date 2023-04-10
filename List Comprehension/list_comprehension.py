# list_comprehension.py
""" List Comprehension """

from time import time

# construct a list from another existing list
# 1. faster for-loops
# 2. simplified conditional statements
# 3. string manipulation

fruits = ["apples", "bananas", "strawberries"]

### printing comparison

# traditional for-loop method
start_time = time()
for fruit in fruits:
    print(fruit)
end_time = time()
time_loop = end_time - start_time
# print(time_loop)    # 0.000024 seconds
print("\n")

# list comprehension method
start_time = time()
[ print(fruit) for fruit in fruits ]
end_time = time()
time_comprehension = end_time - start_time
# print(time_comprehension)   # 0.000005006
print("\n")

if time_comprehension < time_loop:
    print("List comprehension was faster")
else:
    print("For loop was faster")
print("\n")


### string case change comparison

# traditional for-loop method
start_time = time()
new_fruits = []
for fruit in fruits:
    fruit = fruit.upper()
    new_fruits.append(fruit)

fruits = new_fruits
end_time = time()
time_loop = end_time - start_time
# print(time_loop)
print("\n")

# list comprehension method
start_time = time()
fruits = [fruit.upper() for fruit in fruits]
end_time = time()
time_comprehension = end_time - start_time
# print(time_comprehension)
print("\n")

if time_comprehension < time_loop:
    print("List comprehension was faster")
else:
    print("For loop was faster")
print("\n")

