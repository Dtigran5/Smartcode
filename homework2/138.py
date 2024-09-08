keypad = {
    '1': ['.', ',', '?', '!', ':'],
    '2': ['A', 'B', 'C'],
    '3': ['D', 'E', 'F'],
    '4': ['G', 'H', 'I'],
    '5': ['J', 'K', 'L'],
    '6': ['M', 'N', 'O'],
    '7': ['P', 'Q', 'R', 'S'],
    '8': ['T', 'U', 'V'],
    '9': ['W', 'X', 'Y', 'Z'],
    '0': [' ']
}

char_to_keys = {}
for key, chars in keypad.items():
    for index, char in enumerate(chars):
        char_to_keys[char] = key * (index + 1)

def text_to_keypress(text):
    result = []
    for char in text.upper():
        if char in char_to_keys:
            result.append(char_to_keys[char])
    return ''.join(result)

user_input = input("Enter your message: ")
output = text_to_keypress(user_input)
print(output)
