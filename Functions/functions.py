import random
from sty import fg

def generate_RGB():
    """generates random colors"""
    red_int = random.randint(0, 256)
    green_int = random.randint(0, 256)
    blue_int = random.randint(0, 256)
    return red_int, green_int, blue_int

def generate_color(red_value, green_value, blue_value):
    """generate_color docstring"""
    return fg(red_value, green_value, blue_value)

red, green, blue = generate_RGB()
color = generate_color(red, green, blue)
print(color, "I\'m randomly changing colors!\n")


def about_me(name, profession, pet):
    """prints biographical data"""
    print("Hi! My name is", name)
    print("I am a", profession)
    print("and I have a", pet, "\n")

about_me("Ben", "programmer", "cat")
about_me("Gandalf", "wizard", "mighty eagle")
