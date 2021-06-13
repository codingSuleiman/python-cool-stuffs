


import string
import random

alphabet = string.ascii_letters + string.digits

def passwordGenerator(length):
    return  ''.join(random.choice(alphabet) for i in range(length))
    
passwordGenerator(60)



