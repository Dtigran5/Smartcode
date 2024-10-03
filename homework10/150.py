def tail(filename, n=10):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines[-n:]:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    tail(filename)
