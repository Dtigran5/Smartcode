import string
import random

digits = string.digits
alphabet = string.ascii_uppercase

def generate_car_number():
    car_number = ''.join(random.choices(digits, k=4) + random.choices(alphabet, k=3))
    return car_number

def main():
    print(generate_car_number())


if __name__ == '__main__':
    main()