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
just_to_make_pylance_happy = [ print(fruit) for fruit in fruits ]
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


### Creating new lists from old lists

# traditional for-loop method
start_time = time()
bits = [False, True, False, False, True, False, False, True, False]
new_bits = []

for b in bits:
    if b == True:
        new_bits.append(1)
    else:
        new_bits.append(0)
end_time = time()
time_loop = end_time - start_time

# list comprehension method
start_time = time()
super_bits = [1 if b == True else 0 for b in bits]
time_comprehension = end_time - start_time

# print(bits)
# print(new_bits)
# print(super_bits)

if time_comprehension < time_loop:
    print("List comprehension was faster")
else:
    print("For loop was faster")
print("\n")


### String manipulation

MY_STRING = "HelloMyNameIsBen"
# MY_STRING = [ i for i in MY_STRING ]
    # ['H', 'e', 'l', 'l', 'o', 'M', 'y', 'N', 'a', 'm', 'e', 'I', 's', 'B', 'e', 'n']
MY_STRING = "".join(
    [ i if i.islower() else " " + i for i in MY_STRING ]
    )[1:]   # [1:] keeps all items from index 1 to the end, removing the leading space
print(MY_STRING)

# can add an elif into the comprehension, but can't use the elif keyword, so
MY_STRING = "HelloMyNameIsBen"
# MY_STRING = [ i for i in MY_STRING ]
    # ['H', 'e', 'l', 'l', 'o', 'M', 'y', 'N', 'a', 'm', 'e', 'I', 's', 'B', 'e', 'n']
MY_STRING = "".join(
    [ i if i.islower()
     else " " + i.lower() if i in ["M", "N", "I"]
     else " " + i for i in MY_STRING ]
    )[1:]   # [1:] keeps all items from index 1 to the end, removing the leading space
print(MY_STRING)
