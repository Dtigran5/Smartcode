def calculate_median(a, b, c):
    return sorted([a, b, c])[1]

if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))
    
    median = calculate_median(num1, num2, num3)
    print(f"The median value is: {median}")
