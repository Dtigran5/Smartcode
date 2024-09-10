def hex2int(hex_digit):
    if len(hex_digit) != 1 or hex_digit not in '0123456789abcdefABCDEF':
        raise ValueError("Input must be a single hexadecimal digit (0-9, A-F).")
    return int(hex_digit, 16)

def int2hex(decimal_int):
    if decimal_int < 0 or decimal_int > 15:
        raise ValueError("Input must be an integer between 0 and 15.")
    return hex(decimal_int).upper()[2:]

try:
    print(hex2int('A'))  # Output: 10
    print(hex2int('a'))  # Output: 10
    print(int2hex(10))   # Output: A
    print(int2hex(15))   # Output: F
except ValueError as e:
    print(e)