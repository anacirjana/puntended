import random
from string import ascii_uppercase

def generate_roomcode():
    code = ''
    for i in range(0,3):
        code += random.choice(list(ascii_uppercase))
    return code