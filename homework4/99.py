def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def nextPrime(n):
    n += 1
    while not is_prime(n):
        n += 1
    return n

if __name__ == "__main__":
    user_input = int(input("Enter an integer: "))
    print("The first prime number larger than", user_input, "is", nextPrime(user_input))