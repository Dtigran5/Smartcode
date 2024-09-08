def reverseLookup(dictionary, value):
    return [key for key, val in dictionary.items() if val == value]

    
sample_dict = {
        'a': 1,
        'b': 2,
        'c': 1,
        'd': 3
    }
    
    
search_value = 1
result = reverseLookup(sample_dict, search_value)
print(f"Keys for value {search_value}: {result}")

search_value = 2
result = reverseLookup(sample_dict, search_value)
print(f"Keys for value {search_value}: {result}")

search_value = 4
result = reverseLookup(sample_dict, search_value)
print(f"Keys for value {search_value}: {result}")
