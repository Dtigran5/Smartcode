def load_elements(filename):
    elements_by_number = {}
    elements_by_symbol = {}
    elements_by_name = {}

    try:
        with open(filename, 'r') as file:
            for line in file:
                number, symbol, name = line.strip().split(',')
                number = int(number)

                elements_by_number[number] = (symbol, name)
                elements_by_symbol[symbol] = (number, name)
                elements_by_name[name] = (number, symbol)

        return elements_by_number, elements_by_symbol, elements_by_name

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None, None, None
    except PermissionError:
        print(f"Error: Permission denied to access the file '{filename}'.")
        return None, None, None

def main():
    filename = input("Enter the filename containing the chemical elements: ")
    elements_by_number, elements_by_symbol, elements_by_name = load_elements(filename)

    if elements_by_number is None:
        return

    while True:
        user_input = input("Enter an atomic number, symbol, or element name (or press Enter to exit): ")

        if user_input == "":
            break

        try:
            number = int(user_input)
            if number in elements_by_number:
                symbol, name = elements_by_number[number]
                print(f"Element with atomic number {number}: {symbol} ({name})")
            else:
                print(f"No element found with atomic number {number}.")
        except ValueError:
            user_input = user_input.capitalize()
            if user_input in elements_by_symbol:
                number, name = elements_by_symbol[user_input]
                print(f"Element with symbol {user_input}: Atomic number {number}, Name: {name}")
            elif user_input in elements_by_name:
                number, symbol = elements_by_name[user_input]
                print(f"Element with name {user_input}: Atomic number {number}, Symbol: {symbol}")
            else:
                print(f"No element found with symbol or name '{user_input}'.")

if __name__ == "__main__":
    main()
