import string

def load_words(filename):
    try:
        with open(filename, 'r') as file:
            words = file.read().lower().split()
            return words
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return None
    except PermissionError:
        print(f"Error: Permission denied to access the file '{filename}'.")
        return None
    
def count_letter_usage(words):
    letter_usage = {letter: 0 for letter in string.ascii_lowercase}
    
    for word in words:
        cleaned_word = ''.join([char for char in word if char.isalpha()])
        unique_letters_in_word = set(cleaned_word)

        for letter in unique_letters_in_word:
            if letter in letter_usage:
                letter_usage[letter] += 1

    return letter_usage

def main():
    filename = input("Enter the filename containing the list of words: ")
    words = load_words(filename)

    if words is None:
        return

    total_words = len(words)
    if total_words == 0:
        print("No words found in the file.")
        return

    letter_usage = count_letter_usage(words)

    print(f"Proportion of words using each letter (out of {total_words} words):")
    for letter, count in letter_usage.items():
        proportion = (count / total_words) * 100
        print(f"{letter}: {proportion:.2f}%")

    least_used_letter = min(letter_usage, key=letter_usage.get)
    print(f"\nThe letter used in the smallest proportion of words is: '{least_used_letter}'")

if __name__ == "__main__":
    main()
