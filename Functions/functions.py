import random
from sty import fg

def generateRGB():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)
    return red, green, blue

def generateColor(red, green, blue):
    return fg(red, green, blue)

red, green, blue = generateRGB()
color = generateColor(red, green, blue)
print(color, "I\'m randomly changing colors!\n")


def about_me(name, profession, pet):
    print("Hi! My name is", name)
    print("I am a", profession)
    print("and I have a", pet, "\n")

about_me("Ben", "programmer", "cat")
about_me("Gandalf", "wizard", "mighty eagle")