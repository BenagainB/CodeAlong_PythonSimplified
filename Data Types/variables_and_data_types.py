# variables_and_data_types.py

# 8 basic data types

# Numeric data types: integer and float

dragons = 3
dead_dragons = 2

total_dragons = dragons - dead_dragons
print(total_dragons)    # 1

covid_bc = 1203 # covid cases in British Columbia
population_bc = 5071000

prob = covid_bc / population_bc
print(prob) # 0.00023723131532242162

print(type(prob))   # <class 'float'>
print(type(population_bc))  # <class 'int'>

a = 12
b = 3

print(a + b)

# string

pet = "cat"
pet_name = "Neo"
pet_age = "4"

print(pet, pet_name, pet_age)   # cat Neo 4
print("I have a", pet, "his name is", pet_name, "and he is", pet_age, "years old")
print("I have a", pet, "\nhis name is", pet_name, "\nand he is", pet_age, "years old")

my_pet = "my " + pet + "'s name is " + pet_name
print(my_pet)

my_pet2 = "I have a {}, his name is {} and he is {} years old".format(pet, pet_name, pet_age)
print(my_pet2)

a = "coffee"
b = "sugar"

print( a + b)
print(a * 2)
print(b * 5)

