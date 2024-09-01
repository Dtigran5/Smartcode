text = input("Enter the text: ")
vowels = [char for char in text if char.lower() in 'aeiouAEIOU'] 
print("List of vowels:", vowels)
print("List length:", len(vowels))
