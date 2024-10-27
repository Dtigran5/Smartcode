def proper_divisors(n):
    divisors = [i for i in range(1, n) if n % i == 0]
    return divisors

def main():
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        divisors = proper_divisors(n)
        print(f"The proper divisors of {n} are: {divisors}")

if __name__ == "__main__":
    main()
