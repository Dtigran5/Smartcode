import random

def generate_random_password():
    length = random.randint(7, 10)
    password = ''.join(chr(random.randint(33, 126)) for _ in range(length))
    return password

def is_good_password(password):
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

def main():
    attempts = 0
    password = generate_random_password()
    
    while not is_good_password(password):
        attempts += 1
        password = generate_random_password()
    
    print(f"Generated good password: {password}")
    print(f"Number of attempts: {attempts}")

if __name__ == "__main__":
    main()
