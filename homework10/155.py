def most_frequent_words(filename):
    try:
        with open(filename, 'r') as file:
            word_count = {}
            for line in file:
                words = line.split()
                for word in words:
                    cleaned_word = word.strip(".,!?;:()[]{}<>").lower()
                    if cleaned_word:
                        if cleaned_word in word_count:
                            word_count[cleaned_word] += 1
                        else:
                            word_count[cleaned_word] = 1

        if word_count:
            max_frequency = max(word_count.values())
            most_frequent = [word for word, count in word_count.items() if count == max_frequency]
            print(f"The most frequent word(s) (occurring {max_frequency} times):")
            print(", ".join(most_frequent))
        else:
            print("No words found in the file.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    most_frequent_words(filename)
