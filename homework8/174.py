def gcd(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return gcd(b, c)

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
result = gcd(a, b)
print(f"The greatest common divisor of {a} and {b} is: {result}")

