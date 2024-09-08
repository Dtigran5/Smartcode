def count_unique_characters(input_string):
    unique_characters = set(input_string)
    return len(unique_characters)

user_input = input("Enter a string: ")
unique_count = count_unique_characters(user_input)
print(f"The number of unique characters in the string is: {unique_count}")
