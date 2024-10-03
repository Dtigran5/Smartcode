def remove_comments(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()
        
        with open(output_filename, 'w') as outfile:
            for line in lines:
                clean_line = line.split('#')[0].rstrip()
                outfile.write(clean_line + '\n')

        print(f"Comments removed. Modified file saved as '{output_filename}'.")
    
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access the file '{input_filename}' or '{output_filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = input("Enter the name of the input file: ")
    output_file = input("Enter the name of the output file: ")
    remove_comments(input_file, output_file)
