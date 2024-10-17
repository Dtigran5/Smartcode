class LongestWords:
    def __init__(self, input_list):
        self.input_list = input_list
    def find_longest(self):
        max_length = max(len(word) for word in self.input_list)
        return [word for word in self.input_list if len(word) == max_length]

input_list = ["aba", "aa", "ad", "vcd", "aba"]
longest_words = LongestWords(input_list)
print(longest_words.find_longest())