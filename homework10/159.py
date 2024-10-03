import random

def generate_password(word_list):
    valid_words = [word for word in word_list if len(word) >= 3]
    random.shuffle(valid_words)  
    for i in range(len(valid_words)):
        for j in range(i + 1, len(valid_words)):
            word1 = valid_words[i]
            word2 = valid_words[j]
            password = word1 + word2
            if 8 <= len(password) <= 10:
                return password.capitalize()  

    return None  

def main():
    filename = input("Enter the filename containing the list of words: ")
    
    try:
        with open(filename, 'r') as file:
            word_list = file.read().splitlines()
        
        password = generate_password(word_list)
        
        if password:
            print(f"Generated Password: {password}")
        else:
            print("No valid password could be generated with the given word list.")
    
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to access the file '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
