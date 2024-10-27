def correct_capitalization(text):
    corrected_text = ""
    capitalize_next = True
    i = 0
    while i < len(text):
        char = text[i]
        if capitalize_next and char.isalpha():
            corrected_text += char.upper()
            capitalize_next = False
        else:
            if char == 'i' and (i == 0 or text[i - 1] == ' ') and (
                i == len(text) - 1 or text[i + 1] in " .!?,'\""):
                corrected_text += 'I'
            else:
                corrected_text += char

            if char in ".!?":
                capitalize_next = True
            elif not char.isspace():
                capitalize_next = False

        i += 1

    return corrected_text

def main():
    text = input("Enter a sentence: ")
    corrected_text = correct_capitalization(text)
    print("\nCorrected text:")
    print(corrected_text)

if __name__ == "__main__":
    main()
