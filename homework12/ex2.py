class Palindrome:
    def __init__(self, word):
        self.word = word
    def is_palindrome(self):
        return self.word == self.word[::-1]

word = input("Enter word: ")
palindrome = Palindrome(word)
print(palindrome.is_palindrome())