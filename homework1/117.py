import string

def extract_words(input_string):
    punctuation = string.punctuation.replace("'", "") 
    translator = str.maketrans('', '', punctuation)
    cleaned_string = input_string.translate(translator)
    return cleaned_string.split()

user_input = input("Please enter a string: ")
words = extract_words(user_input)
print(words)
