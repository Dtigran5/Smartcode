import random

def generate_random_password():
    length = random.randint(7, 10)
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    return password

if __name__ == "__main__":
    print(generate_random_password())
