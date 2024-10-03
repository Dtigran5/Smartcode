def analyze_frequency(filename):
    try:
        with open(filename, 'r') as file:
            letter_frequencies = {}
            for line in file:
                for char in line:
                    char = char.lower()
                    if char.isalpha():
                        if char in letter_frequencies:
                            letter_frequencies[char] += 1
                        else:
                            letter_frequencies[char] = 1
        
        if letter_frequencies:
            sorted_frequencies = sorted(letter_frequencies.items(), key=lambda x: x[1], reverse=True)
            print("Letter frequencies (sorted by frequency):")
            for letter, frequency in sorted_frequencies:
                print(f"{letter}: {frequency}")
        else:
            print("No alphabetic characters found in the file.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")

if __name__ == "__main__":
    filename = input("Enter the filename to analyze: ")
    analyze_frequency(filename)
