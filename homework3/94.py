def can_form_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return a < b + c and b < a + c and c < a + b

def main():
    lengths = input("Enter three lengths separated by spaces: ").split()
    a, b, c = map(float, lengths)
    if can_form_triangle(a, b, c):
        print("The lengths can form a triangle.")
    else:
        print("The lengths cannot form a triangle.")

if __name__ == "__main__":
    main()
