import random
import string


def generate():
    return random.randint(0, 2000)


def namegenerate(length):
    name = ""
    for i in range(length):
        name += random.choice(string.ascii_letters)

    return name.lower()
