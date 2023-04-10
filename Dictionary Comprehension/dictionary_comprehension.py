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
    "Spider": "photographer",
    "Bat": "philanthropist",
    "Wonder Wo": "nurse"
}
print("modify dictionary in place")
print(my_dict)
# my_dict = {key+"man" : val for (key, val) in my_dict.items()}
# my_dict = {(key+"man" if key != "Spider" else "Superman") : val
#            for (key, val) in my_dict.items()}
my_dict = {(key+"man" if key != "Spider" else "Superman") :
           (val if val != "photographer" else "reporter")
           for (key, val) in my_dict.items()}
print(my_dict)
