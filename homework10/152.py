def add_line_numbers(input_file, output_file):
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line_number, line in enumerate(infile, start=1):
                outfile.write(f"{line_number}: {line}")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access the file '{input_file}'.")
        
def main():
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")
    add_line_numbers(input_file, output_file)
    print(f"Lines from '{input_file}' have been written to '{output_file}' with line numbers.")

if __name__ == "__main__":
    main()
