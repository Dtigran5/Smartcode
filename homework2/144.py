import re

def are_anagrams(str1, str2):
    str1_cleaned = re.sub(r'[\W_]+', '', str1.lower())
    str2_cleaned = re.sub(r'[\W_]+', '', str2.lower())
    
    return sorted(str1_cleaned) == sorted(str2_cleaned)

phrase1 = "William Shakespeare"
phrase2 = "I am a weakish speller"
result = are_anagrams(phrase1, phrase2)
print(result)  
