def phonetic_spelling(word, index=0):
    phonetic_alphabet = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
        'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
        'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
        'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
        'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
        'Y': 'Yankee', 'Z': 'Zulu'
    }
    
    if index < len(word):
        char = word[index].upper()
        if char in phonetic_alphabet:
            return phonetic_alphabet[char] + ' ' + phonetic_spelling(word, index + 1)
        else:
            return phonetic_spelling(word, index + 1)
    return ''

user_input = input("Enter a word: ")
result = phonetic_spelling(user_input)
print(result.strip())
