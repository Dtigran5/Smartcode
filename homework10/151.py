def cat(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    cat(filename)
