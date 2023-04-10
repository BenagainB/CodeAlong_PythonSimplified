# rules_of_naming_variables
"""The Rules of Naming Variables in Python"""

# 1. variable names cannot start with a number

# 1st_greeting = "hello"
# print(1st_greeting)
# File "/CodeAlong_PythonSimplified/Data Types/rules_of_naming_variables.py", line 5
#    1st_greeting = "hello"
#     ^
# SyntaxError: invalid syntax


# 2. variable names can only contain A-Z, a-z, 0-9, and _

# second-greeting = "hello"
# print(second-greeting)
#   File "/CodeAlong_PythonSimplified/Data Types/rules_of_naming_variables.py", line 15
#    second-greeting = "hello"
#    ^
# SyntaxError: cannot assign to operator

third_gr33ting = "hello"
print(third_gr33ting)
# hello


# 3. variable names are case-sensitive

Fourth_greeting = "hi"
print(Fourth_greeting)
# hi

# print(fourth_greeting)
#   File "/CodeAlong_PythonSimplified/Data Types/rules_of_naming_variables.py", line 31, in <module>
#    print(fourth_greeting)
# NameError: name 'fourth_greeting' is not defined


# 4. variable names cannot use Python's reserved keywords

reserved_keywords = ["and", "as", "assert", "break", "class", "continue", "def",
                     "del", "elif", "else", "except", "exec", "finally", "for",
                     "from", "global", "if", "import", "in", "is", "lambda",
                     "not", "or", "pass", "print", "raise", "return", "try",
                     "while", "with", "yield"]

for word in reserved_keywords:
    print(word)

type = 8
print(type)
# 8

# while 'type' is not an official reserved keyword (as seen above), it introduces errors in some cases

# print(type(type))
# Traceback (most recent call last):
#   File "/Users/burbank/Documents/CodeAlong_PythonSimplified/Data Types/rules_of_naming_variables.py", line 53, in <module>
#     print(type(type))
# TypeError: 'int' object is not callable

# the word 'print' has similar issues, so it's best to not use it as a variable name
