import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

if __name__ == "__main__":
    side_a = float(input("Enter the length of the first shorter side: "))
    side_b = float(input("Enter the length of the second shorter side: "))
    hypotenuse = calculate_hypotenuse(side_a, side_b)
    print(f"The length of the hypotenuse is: {hypotenuse}")
