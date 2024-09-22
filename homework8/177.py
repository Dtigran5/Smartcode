def roman_to_int(roman):
    if not roman:
        return 0
    
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    if len(roman) == 1:
        return roman_values[roman]
    
    first_value = roman_values[roman[0]]
    second_value = roman_values[roman[1]]
    
    if first_value < second_value:
        return roman_to_int(roman[2:]) + (second_value - first_value)
    else:
        return roman_to_int(roman[1:]) + first_value

if __name__ == "__main__":
    user_input = input("Enter a Roman numeral: ")
    result = roman_to_int(user_input)
    print(f"The integer value of {user_input} is {result}.")
