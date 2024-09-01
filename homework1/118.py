user_input = input("Enter a string: ")
cleaned_input = ''.join(char.lower() for char in user_input if char.isalnum())
is_palindrome = cleaned_input == cleaned_input[::-1]

if is_palindrome:
    print("The string is a verbal palindrome.")
else:
    print("The string is not a verbal palindrome.")
