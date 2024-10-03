def longest_word(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            longest_word = ''
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word
            return longest_word
    except FileNotFoundError as e:
        print(e)

filename = 'input1.txt'
result = longest_word(filename)
print(result)