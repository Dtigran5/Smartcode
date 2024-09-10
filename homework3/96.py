def isInteger(s):
    s = s.strip()
    if len(s) == 0:
        return False
    if s[0] in ('+', '-'):
        return len(s) > 1 and s[1:].isdigit()
    return s.isdigit()

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    if isInteger(user_input):
        print(f'"{user_input}" represents a valid integer.')
    else:
        print(f'"{user_input}" does not represent a valid integer.')
