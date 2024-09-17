#link -> https://www.codewars.com/kata/52fba66badcd10859f00097e
def disemvowel(comment):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in comment if char not in vowels)

comment = "This website is for losers LOL!"
result = disemvowel(comment)
print(result)  
