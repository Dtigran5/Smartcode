def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '^':
        return 3
    else:
        return -1

if __name__ == "__main__":
    user_input = input("Enter a mathematical operator: ")
    result = precedence(user_input)
    if result != -1:
        print(f"The precedence of '{user_input}' is: {result}")
    else:
        print("Error: The input is not a valid operator.")
