import math

class NameNumber:
    def __init__(self,name):
        self.name = name.lower()
    
    def calculate_name_number(self):
        letter_to_number = {
            'a': 1, 'j': 1, 's': 1,
            'b': 2, 'k': 2, 't': 2,
            'c': 3, 'l': 3, 'u': 3,
            'd': 4, 'm': 4, 'v': 4,
            'e': 5, 'n': 5, 'w': 5,
            'f': 6, 'o': 6, 'x': 6,
            'g': 7, 'p': 7, 'y': 7,
            'h': 8, 'q': 8, 'z': 8,
            'i': 9, 'r': 9
        }
        name_number = sum(letter_to_number[char] for char in self.name if char in letter_to_number)
        if math.sqrt(name_number) < 5:
            return name_number, "Yes"
        else:
            return name_number, "No"

name = input("Enter your name: ")
name_test = NameNumber(name)
print(name_test.calculate_name_number())
