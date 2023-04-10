# dictionary_comprehension.py
""" Dictionary Comprehension - Create Complex Data Structures Step by Step """

# Create dictionaries from: lists, tuples, dataframes

# Modify dictionaries in place

# Create complex data structures: dictionary of lists, list of dictionaries

names = ['Mariya', 'Gendalf', 'Batman']
profs = ['programmer', 'wizard', 'superhero']

my_dict = {}


def for_loop_zip(list1, list2):
    """ for-loop zip function """
    for (key, value) in zip(list1, list2):
        my_dict[key] = value
    print(my_dict)  # {'Mariya': 'programmer', 'Gendalf': 'wizard', 'Batman': 'superhero'}

print("for-loop zip function")
for_loop_zip(names, profs)
print("\n")

def for_loop_range(list1, list2):
    """ for-loop range function """
    for i in range(min(len(list1), len(list2))):
        my_dict[list1[i]] = list2[i]
    print(my_dict)

print("for-loop range function")
for_loop_range(names, profs)

# modify dictionary in place
my_dict = {
    "spider": "photographer",
    "Bat": "philanthropist",
    "Wonder Wo": "nurse"
}
print(my_dict)